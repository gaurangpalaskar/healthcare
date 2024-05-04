from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse("hello world!")

def dashboard(request):
    return render(request,"dashboard.html")