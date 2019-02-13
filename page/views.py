from django.shortcuts import render
from django.http import HttpResponse
from .models import User

def index(request):
    # return HttpResponse('Hello world!')
    return render(request, 'page/index.html')

def home(request):

    return render(request, 'page/home.html')

