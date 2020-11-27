from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def index(request):
    return HttpResponse("Hell Yeah!")


def index2(request):
    return HttpResponse('<em>My Second App</em>')


def index3(request):
    my_dict = {'insert_me': 'Hello ! I am from first_app/index.html'}
    return render(request, 'first_app/index.html', context=my_dict)


def helps(request):
    key = {'key': 'Help Page'}
    return render(request, 'first_app/help.html', context=key)


def me(request):
    key = {'key': 'Help Page'}
    return render(request, 'first_app/photo.html', context=key)
