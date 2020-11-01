from django.urls import path
from . import views

app_name = 'homepage'

urlpatterns = [
    path('privacy/', views.privacy, name='privacy'),
    path('', views.index, name='index')
]