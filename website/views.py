from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse("hello world!")

def dashboard(request):
    context = {"numbers" : [1,2,3,4,5] ,
    "names" : ['gaurang','ankita','sachin sir','faheem']
    }
    return render(request,"dashboard.html",context)

def home(request):
    message1 = "welcome to home page from views.py"
    data = {'message1':message1}    
    return render(request,"home.html",data) 