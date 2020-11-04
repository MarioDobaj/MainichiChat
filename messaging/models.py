import datetime
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Message(models.Model):
    conversation_id = models.CharField(max_length=100)
    datetime = models.DateTimeField(auto_now=False)
    sender_id = models.IntegerField(default=-1)
    receiver_id = models.IntegerField(default=-1)
    sender_user = models.ForeignKey(User, on_delete=models.CASCADE, blank = True,null=True, related_name = 'sender_user')
    receiver_user = models.ForeignKey(User, on_delete=models.CASCADE, blank = True,null=True, related_name = 'receiver_user')
    text = models.CharField(max_length=500)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return self.conversation_id