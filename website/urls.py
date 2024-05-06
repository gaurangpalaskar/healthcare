from django.contrib import admin
from django.urls import path

from .views import index,dashboard,home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', index),
    path('dashboard/', dashboard , name="dashboard-page"),    # name is a unique identifier for URL pattern 
    path('home/', home , name="home-page"),
]

