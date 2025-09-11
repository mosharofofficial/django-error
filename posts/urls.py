from django.urls import path
from posts.views import *

app_name = 'posts'

urlpatterns = [
    path('', postList, name='posts'),
    path('<slug:slug>', postPage, name='page'),
]
