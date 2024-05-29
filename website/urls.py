from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("", include("clinic.urls")),
    # /admin/
    path("admin/", admin.site.urls),
    # /core/
    path("core/", include("core.urls")),
    # /accounts/
    path("accounts/", include("accounts.urls")),
]
