import datetime
from django.conf import settings
from django.db import models
import twit.twitter
from twit.util.models import TrackedModel

class User(TrackedModel):
    id = models.IntegerField(primary_key=True, unique=True, editable=False, db_index=True)
    screen_name = models.SlugField(unique=True, max_length=30, db_index=True)
    description = models.CharField(max_length=500, blank=True, null=True)
    followers_count = models.PositiveIntegerField(default=0)
    friends_count = models.PositiveIntegerField(default=0)
    location = models.CharField(max_length=50, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, db_index=True, null=True)
    background_color = models.CharField(max_length=10, blank=True, null=True)
    background_img = models.URLField(max_length=255, blank=True, null=True)
    protected = models.BooleanField(default=False)
    url = models.URLField(max_length=255, blank=True, null=True)
    tz = models.CharField(max_length=255, blank=True, null=True)
    utc_offset = models.IntegerField(default=0)

    friends = models.ManyToManyField('api.User')
    
    def get_friends(self, api):
        friends = api.GetAllFriends(user = self.screen_name)
        flist = []
        for api_friend in friends:
            friend = User.from_api(api_friend)
            self.friends.add(friend)
            flist.append(friend)
        return flist

    def get_followers(self, api):
        friends = api.GetAllFollowers(user = self.screen_name)
        flist = []
        for api_friend in friends:
            friend = User.from_api(api_friend)
            self.friends.add(friend)
            flist.append(friend)
        return flist

    def refresh(self, api, commit=True, using=None):
        user = api.GetUser(self.screen_name)
        self.set_data(user)
        if commit:
            self.save(using=using)

    def set_data(self, user):
        self.screen_name = user.screen_name
        self.description = user.description
        self.followers_count = user.followers_count
        self.id = user.id
        self.location = user.location
        self.name = user.name
        self.background_color = user.profile_background_color
        self.background_img =user.profile_background_image_url
        self.protected = user.protected
        self.url = user.url
        self.tz = user.time_zone
        self.utc_offset = user.utc_offset

    @classmethod
    def lookup(cls, api, screen_name, *args, **kwargs):
        return User.from_api(api.GetUser(screen_name), *args, **kwargs)

    @classmethod
    def from_api(cls, user, commit=True, using=None):
        try:
            return User.objects.get(id=user.id)
        except User.DoesNotExist:
            account = User()
            account.set_data(user)
            if commit:
                account.save(using=using)
            return account

class List(TrackedModel):
    '''A class representing the List structure used by the twitter API.
    '''
    id = models.IntegerField(primary_key=True, unique=True, editable=False, db_index=True)
    name = models.SlugField(unique=True, max_length=30, db_index=True)
    slug = models.SlugField(unique=True, max_length=30, db_index=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    full_name = models.CharField(max_length=255, null=True)
    mode = models.CharField(max_length=50, null=True)
    uri = models.CharField(max_length=255, null=True)
    member_count = models.PositiveIntegerField(default=0)
    subscriber_count = models.PositiveIntegerField(default=0)
    following = models.BooleanField(default=False)
    members = models.ManyToManyField('api.User')

    def refresh(self, api, commit=True, using=None):
        obj = api.GetList(self.uri)
        self.set_data(obj)
        if commit:
            self.save(using=using)

    def set_data(self, lst):
        self.screen_name = lst.screen_name
        self.description = lst.description
        self.followers_count = lst.followers_count
        self.id = lst.id
        self.location = lst.location
        self.name = lst.name
        self.background_color = lst.profile_background_color
        self.background_img =lst.profile_background_image_url
        self.protected = lst.protected
        self.url = lst.url
        self.tz = lst.time_zone
        self.utc_offset = lst.utc_offset

    def load_members(self, api):
        members = api.GetAllListMembers(self.uri)
        for member in members:
            user = TwitterAccount.from_api(member)
            self.members.add(user)

    @classmethod
    def lookup(cls, api, uri, *args, **kwargs):
        return List.from_api(api.GetList(uri), *args, **kwargs)

    @classmethod
    def from_api(cls, lst, commit=True, using=None):
        try:
            return List.objects.get(id=lst.id)
        except List.DoesNotExist:
            new_list = List()
            new_list.set_data(lst)
            if commit:
                new_list.save(using=using)
            return new_list

class Url(TrackedModel):
    url = models.URLField(verify_exists=False)
    expanded_url = models.URLField(verify_exists=False, null=True)

class Status(TrackedModel):
    id = models.IntegerField(primary_key=True, unique=True, editable=False, db_index=True)
    user = models.ForeignKey('api.User', related_name='user_status_set')
    created_at = models.DateTimeField(null=True)
    favorited = models.BooleanField(default=False)
    in_reply_to_screen_name = models.CharField(max_length=50, blank=True, null=True)
    in_reply_to_user_id = models.PositiveIntegerField(null=True)
    in_reply_to_status_id = models.PositiveIntegerField(null=True)
    truncated = models.BooleanField(default=False)
    source = models.CharField(max_length=255, null=True)
    text = models.CharField(max_length=200)
    location = models.CharField(max_length=255, null=True)
    urls = models.ManyToManyField('api.Url')
    contributors = models.ManyToManyField('api.User', related_name='user_contributors_set')

    def set_data(self, status):
        saved = bool(self.pk)
        self.id = status.id
        self.created_at = datetime.datetime.fromtimestamp(status.created_at)
        self.favorited = status.favorited
        self.in_reply_to_screen_name = status.in_reply_to_screen_name
        self.in_reply_to_user_id = status.in_reply_to_user_id
        self.in_reply_to_status_id = status.in_reply_to_status_id
        self.truncated = status.truncated
        self.source = status.source
        self.text = status.text
        self.location = status.location
        self.user = User.from_api(status.user)
        if saved:
            self.add_many_to_many(status)

    def add_urls(self, status):
        for api_url in status.urls:
            url = Url.from_api(api_url)
            if not self.urls.filter(url=url.url):
                self.urls.add(url)

    def add_contributors(self, status):
        for api_user in status.contributors:
            user = User.from_api(api_user)
            if not self.contributors.filter(id=user.id):
                self.contributors.add(user)

    def add_many_to_many(self, status):
        self.add_urls(status)
        self.add_contributors(status)

    @classmethod
    def from_api(cls, status, commit=True, using=None):
        try:
            return Status.objects.get(id=status.id)
        except Status.DoesNotExist:
            new_status = Status()
            new_status.set_data(lst)
            if commit:
                new_status.save(using=using)
            return new_status
