from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from datetime import datetime

from django.contrib.auth.models import User
from .models import Message
from .serializers import UserSerializer
from .serializers import MessageSerializer



@login_required(login_url='/')
def index(request):
    serializer_class = UserSerializer
    usersQueryset = User.objects.all()

    context = {
    }
    return render(request, 'messaging/messaging.html', context)

class UsersList(generics.ListAPIView):
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        user_id = self.request.user.id

        queryset = User.objects.all().exclude(id=user_id)
        return queryset

class MessagesList(generics.ListAPIView):
    serializer_class = MessageSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        print('message read started')
        user_id = self.request.user.id
        
        queryset = Message.objects.all()
        queryset = queryset.filter(sender_id = user_id) | queryset.filter(receiver_id = user_id)
        queryset = queryset.order_by('datetime', 'id')
        print('message read end?')
        return queryset

class NewMessage(generics.ListAPIView):
    serializer_class = MessageSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        user_id = self.request.user.id

        sender_id = self.kwargs.get('sender_id', "")
        receiver_id = self.kwargs.get('receiver_id', "")
        message_text = self.kwargs.get('message_text', "")
        dt = datetime.now()
        d_truncated = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)

        if str(user_id) != str(sender_id):
            return Message.objects.none()

        if sender_id<receiver_id:
            conversation_id = str(receiver_id)+'_'+str(sender_id)
        else:
            conversation_id = str(sender_id)+'_'+str(receiver_id)

        if conversation_id == "0_0":
            return Message.objects.none()

        sender = User.objects.get(id=sender_id)
        receiver = User.objects.get(id=receiver_id)

        new_message, created = Message.objects.get_or_create(conversation_id=conversation_id, datetime=d_truncated, sender_id=sender_id, receiver_id=receiver_id, sender_user=sender, receiver_user=receiver, text=message_text)
        new_message.save()
        
        return Message.objects.none()