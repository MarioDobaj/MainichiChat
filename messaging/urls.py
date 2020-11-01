from django.urls import path
from . import views

app_name = 'messaging'

urlpatterns = [
    # ex: /messaging/
    path('', views.index, name='index'),
    # ex: /messaging/5/
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /messaging/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /messaging/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]