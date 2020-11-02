import datetime
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User



class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

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