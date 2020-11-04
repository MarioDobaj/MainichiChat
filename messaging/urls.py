from django.urls import path, re_path
from .views import index, UsersList, MessagesList, NewMessage

app_name = 'messaging'

urlpatterns = [
    path('api/users/', UsersList.as_view(), name='users_api'),
    path('api/user_messages/', MessagesList.as_view(), name='messages_list_api'),
    path('api/new_message/<int:sender_id>/<int:receiver_id>/(?P<message_text>[-\w]+)/', NewMessage.as_view(), name='new_message_api'),
    path('', index, name='index'),
]