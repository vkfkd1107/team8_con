from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponseRedirect,HttpResponse

# Create your views here.

def home(request):
    return redirect('https://pjrunup.herokuapp.com/')

def move(request):
    return redirect('https://www.naver.com/')