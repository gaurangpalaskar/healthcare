from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import Department,Employees
from .forms import DepartmentForm,EmployeesForm

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

def get_employee_info(request):
    employees = Employees.objects.all()
    context = {"emps" : employees}                         
    return render(request,"core/employees.html",context)

def whatsmyname(request,name):
    context = {"name" : name}                         
    return render(request,"core/hello.html",context)

def department_details(request,dept_id):
    department = Department.objects.get(dept_id=dept_id)
    context = {"department" : department}                         
    return render(request,"core/department_details.html",context)

def create_department(request):

    if request.method == "POST":
        form = DepartmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("core:departments")
    else:
        form = DepartmentForm

    context = {"form" : form}
    return render(request,"core/create_department.html",context)

def create_employee(request):

    if request.method == "POST":
        form = EmployeesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("core:employees")
    else:
        form = EmployeesForm

    context = {"form" : form}
    return render(request,"core/create_employee.html",context)