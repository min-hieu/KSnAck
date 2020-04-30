from django.db import models
from uuid import uuid1

class transaction(models.Model):
    
    class Status(models.IntegerChoices):
        PROCESSING = 0
        DELIVERED = 1
        FAILED = 2
        IN_QUEUE = 3

    status = models.IntegerField(default=3,choices=Status.choices)
    food_id             = models.UUIDField(default=uuid1)
    date_create         = models.DateTimeField(verbose_name='date created', auto_now_add=True)
    date_update         = models.DateTimeField(verbose_name='date update', auto_now=True)
    category            = models.CharField(blank=False,null=False,default='general',max_length=200)
    tags                = models.TextField(blank=True,null=True)
    donor               = models.CharField(max_length=100,null=False)
    recipient           = models.CharField(max_length=100,null=False, default='None :(')
    details             = models.TextField(blank=True,null=True)
    title               = models.CharField(default='Help!',max_length=60,null=True)
