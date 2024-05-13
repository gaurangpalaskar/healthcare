from django.http import HttpResponse
from django.shortcuts import render
from .models import Department

def index(request):
    return HttpResponse("hello world!")

def dashboard(request):
    context = {"numbers" : [1,2,3,4,5] ,
    "names" : ['gaurang','ankita','sachin sir','faheem']
    }
    return render(request,"core/dashboard.html",context)

def home(request):
    message1 = "welcome to home page from views.py"
    data = {'message1':message1}    
    return render(request,"core/home.html",data) 

def testing(request):
    return render(request,"core/testing.html")

def get_departments(request):
    departments = Department.objects.all()
    context = {"depts" : departments}
    return render(request,"core/departments.html",context)




