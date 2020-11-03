from django.urls import path
from . import views

app_name = 'homepage'

urlpatterns = [
    path('privacy/', views.privacy, name='privacy'),
    path('register/', views.register, name='register'),
    path('', views.index, name='index')
]