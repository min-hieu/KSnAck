from django.db import models
from uuid import uuid1

class food_transaction(models.Model):
    # class Status(models.IntegerChoices):
    #     PROCESSING = 0
    #     DELIVERED = 1
    #     FAILED = 2
    #     IN_QUEUE = 3

    # status = models.IntegerField(default=3,choices=Status.choices)
    food_id = models.UUIDField(default=uuid1)
    category = models.CharField(blank=False,null=False,default='general',max_length=200)
    tags = models.TextField(blank=True,null=True)
    donor = models.CharField(max_length=100,null=False)
    recipient = models.CharField(max_length=100,null=False)
    details = models.TextField(blank=True,null=True)