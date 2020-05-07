from django.db import models
from uuid import uuid1
from taggit.managers import TaggableManager

class transaction(models.Model):
    
    class Status(models.IntegerChoices):
        PROCESSING = 0
        DELIVERED = 1
        FAILED = 2
        IN_QUEUE = 3
        CANCELLED = 4

    class Methods(models.IntegerChoices):
        DONATION = 0
        TRADE = 1

    status              = models.IntegerField(default=3,choices=Status.choices)
    food_id             = models.UUIDField(default=uuid1)
    date_create         = models.DateTimeField(verbose_name='date created', auto_now_add=True)
    date_update         = models.DateTimeField(verbose_name='date update', auto_now=True)
    tags                = TaggableManager()
    donor               = models.CharField(max_length=100,null=False,default='None')
    recipient           = models.CharField(max_length=100,null=False,default='None')
    details             = models.TextField(blank=True,null=True)
    title               = models.CharField(default='Help!',max_length=60,null=True)
    give                = models.CharField(max_length=100,null=False)
    want                = models.CharField(max_length=100,null=False, default=None)
    method              = models.IntegerField(default=0,choices=Methods.choices)
    author              = models.CharField(max_length=100, blank=False)

    def __str__(self):
        return '%s for %s' % (self.title, self.author)
