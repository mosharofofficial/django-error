from django.shortcuts import render
from posts.models import *
from django.http import HttpResponse
# Create your views here.


def postList(request):
    posts = Posts.objects.all().order_by('title')
    return render(request, './postList.html', {'posts': posts})


def postPage(request, slug):
    return HttpResponse( slug)
