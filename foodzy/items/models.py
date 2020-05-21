from django.db import models
from uuid import uuid1
from taggit.managers import TaggableManager

class transaction(models.Model):
    
    class Status(models.IntegerChoices):
        PROCESSING  = 0
        SUCCESS     = 1
        FAILED      = 2
        IN_QUEUE    = 3

    class Method(models.IntegerChoices):
        REQUEST     = 0
        OFFER       = 1

    status              = models.IntegerField(default=3,choices=Status.choices,null=False)
    date_create         = models.DateTimeField(verbose_name='date created', auto_now_add=True)
    date_update         = models.DateTimeField(verbose_name='date update', auto_now=True)
    tags                = TaggableManager()
    author              = models.CharField(max_length=100, null=False)
    accepter            = models.CharField(default='None', max_length=100, null=False)
    title               = models.CharField(max_length=60, null=False)
    content             = models.CharField(max_length=100, null=False)
    details             = models.TextField(blank=True, null=True)
    method              = models.IntegerField(default=0,choices=Method.choices,null=False)

    def __str__(self):
        return '%s for %s' % (self.title, self.author)


