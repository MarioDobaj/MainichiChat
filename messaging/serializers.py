from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Message
import datetime


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email')

class MessageSerializer(serializers.ModelSerializer):
    sender_user = UserSerializer()
    receiver_user = UserSerializer()
    datetime = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")

    class Meta:
        model = Message
        fields = ('id', 'conversation_id', 'datetime', 'sender_id', 'receiver_id', 'sender_user', 'receiver_user', 'text', 'is_read')