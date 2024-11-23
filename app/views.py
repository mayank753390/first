from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def mayank(request):
    return HttpResponse('mayank is a Brave Boy Who know Everything')

def Raman(request):
    return HttpResponse('<h1>Raman have passed intermediate in 2018</h1>')

def Aman(request):
    return HttpResponse('<h1><marquee>Aman a very Hardworking and Dedicated Person </marquee></h1>')
