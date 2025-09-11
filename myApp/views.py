from django.shortcuts import render

# Create your views here.


def index(req):
    return render(req, "index.html")


def about(request):
    return render(request, "about.html")


def contact(request):
    return render(request, "contact.html")


def login(req):
    return render(req, 'login.html')


