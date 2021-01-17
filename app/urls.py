from django.urls import path
from app import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('hashtag/', views.HashtagView.as_view(), name='hashtag'),
]
