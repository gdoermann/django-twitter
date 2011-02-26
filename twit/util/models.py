from django.db import models
import datetime

class TrackedModel(models.Model):
    """
    It would be nice to add some signal receivers and tack who is actually making the changes
    by processing who is logged in each time a model is changed.  It would be better to have a
    different table where a new log is added for each time the item is changed and what fields
    are changed.
    """
    created = models.DateTimeField(auto_now_add=True, default = datetime.datetime.now)
    modified = models.DateTimeField(auto_now=True, default = datetime.datetime.now)

    class Meta:
        abstract = True
