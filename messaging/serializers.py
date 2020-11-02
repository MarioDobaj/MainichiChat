from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Message

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'email')

class MessageSerializer(serializers.ModelSerializer):
    sender_user = UserSerializer()
    receiver_user = UserSerializer()

    class Meta:
        model = Message
        fields = ('id', 'conversation_id', 'datetime', 'sender_id', 'receiver_id', 'sender_user', 'receiver_user', 'text', 'is_read')