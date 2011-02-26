from django.db import models
from django.db.utils import IntegrityError
from accounts.models import TrackedModel

USER = 0
LIST = 1
USER_TYPE_CHOICES = (
    (USER, "User"),
    (LIST, 'List'),
)

class UserOrList(TrackedModel):
    name = models.CharField(max_length=30)
    slug = models.CharField(max_length=30, unique=True, db_index=True)
    obj_type = models.IntegerField(choices = USER_TYPE_CHOICES, default=USER, db_index=True)
    user = None # Foreign Key
    lst = None # Foreign Key
    members = None # Many To Many

    def object(self):
        if self.obj_type == LIST:
            return self.lst
        else:
            return self.user

    def member_count(self):
        return self.members.count()

    def load_members(self, api):
        if not self.user or self.lst:
            return
        if self.lst:
            if not self.lst.members.all():
                self.lst.load_members(api)
            users = self.lst.members.all()
        else:
            if not self.user.friends.all():
                self.user.get_friends(api)
            users = self.user.friends.all()
        
        for member in users:
            if not self.members.filter(id=member.id):
                self.members.add(member)

    def save(self, *args, **kwargs):
        if self.obj_type == USER and not self.user:
            raise IntegrityError("You must specify a user.")
        if self.obj_type == LIST and not self.lst:
            raise IntegrityError("You must specify a list.")
        if self.user is None and self.lst is None:
            raise IntegrityError("You must specify a user or a list")
        super(UserOrList, self).save(*args, **kwargs)
        if not self.members.all():
            self.load_members()

    class Meta:
        abstract=True

class Location(UserOrList):
    user = models.ForeignKey('api.User', null=True, related_name="user_location_set")
    lst = models.ForeignKey('api.List', null=True, related_name="list_location_set")
    members = models.ManyToManyField('api.User', related_name = 'user_location_member_set')


class Interest(UserOrList):
    user = models.ForeignKey('api.User', null=True, related_name="user_interest_set")
    lst = models.ForeignKey('api.List', null=True, related_name="list_interest_set")
    members = models.ManyToManyField('api.User', related_name = 'list_location_member_set')
