import datetime
from django.conf import settings
from django.db import models
import twitter
from api.models import User
from util.models import TrackedModel

class UserProfile(TrackedModel):
    """ A user that can login to the program and into twitter """
    user = models.OneToOneField('auth.User')
    screen_name = models.CharField(max_length=30)
    account = models.OneToOneField('api.User')

    access_key = models.CharField(max_length=255, blank=True)
    access_secret = models.CharField(max_length=255, blank=True)

    def api(self, **kwargs):
        return twitter.Api(consumer_key=settings.CONSUMER_KEY, consumer_secret=settings.CONSUMER_SECRET,
                           access_token_key=self.access_key, access_token_secret=self.access_secret, **kwargs)

    def save(self, *args, **kwargs):
        try:
            assert self.account
        except Exception:
            account = self.api().VerifyCredentials()
            account.save()
            self.account = account
        super(UserProfile, self).save(*args, **kwargs)
