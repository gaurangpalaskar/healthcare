from django.contrib import admin
from django.urls import path

from core.views import index,dashboard,home,testing,get_departments

app_name = "core"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', index),
    path('dashboard/', dashboard , name="dashboard-page"),    # name is a unique identifier for URL pattern 
    path('home/', home , name="home-page"),
    path('testing/', testing , name="testing"),
    path('departments/', get_departments , name="departments"),
]

