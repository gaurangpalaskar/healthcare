from django.contrib import admin
from django.urls import path

from core.views import index,dashboard,home,testing,get_departments,get_employee_info,whatsmyname,department_details,create_department,create_employee

app_name = "core"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', index),
    path('dashboard/', dashboard , name="dashboard-page"),    # name is a unique identifier for URL pattern 
    path('home/', home , name="home-page"),
    path('testing/', testing , name="testing"),
    path('departments/', get_departments , name="departments"),
    path('employees/', get_employee_info , name="employees"),
    path("hello/<str:name>/", whatsmyname , name="whatsmyname"),
    path("departments/<int:dept_id>/", department_details , name="department_details"),
    path('departments/create/', create_department , name="create_departments"),
    path('employees/create/', create_employee , name="create_employee"),
]

