from django.urls import path
from posts.views import *



urlpatterns = [
    path('', postList, name='posts'),
    path('<slug:slug>', postPage, name='page'),
]
