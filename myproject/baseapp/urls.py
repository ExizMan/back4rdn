from django.urls import path
from .views import *
from django.urls import re_path as url

urlpatterns = [
    path('',TopicView.as_view(),name='index'),
]
