from django.contrib import admin

from .models import Speciality,Doctor,Patient,Staff

admin.site.register(Speciality)
admin.site.register(Doctor)
admin.site.register(Patient)
admin.site.register(Staff)