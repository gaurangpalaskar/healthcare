from django.contrib import admin
from django.urls import path

from core.views import index

app_name = "accounts"

urlpatterns = [
    path('index/', index),
]

