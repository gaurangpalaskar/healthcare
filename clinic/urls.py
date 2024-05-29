from django.urls import path

from . import views

app_name = "clinic"

urlpatterns = [
    # /
    path("", views.dashboard, name="dashboard"),
    # /specialities/
    path("specialities/", views.get_specialities, name="specialities"),
    # /speciality/<int:id>/
    path("speciality/<int:id>/", views.get_speciality, name="get_speciality"),
    # /speciality/new/
    path("speciality/new/", views.new_speciality, name="new_speciality"),
    # /doctors/
    path("doctors/", views.get_doctors, name="doctors"),
    # /doctor/<int:id>/
    path("doctor/<int:id>/", views.get_doctor, name="get_doctor"),
    # /doctor/new/
    path("doctor/new/", views.new_doctor, name="new_doctor"),
    # /patients/
    path("patients/", views.get_patients, name="patients"),
    # /patient/<int:id>/
    path("patient/<int:id>/", views.get_patient, name="get_patient"),
    # /patient/new/
    path("patient/new/", views.new_patient, name="new_patient"),
    # /staffs/
    path("staffs/", views.get_staffs, name="staffs"),
    # /staff/<int:id>/
    path("staff/<int:id>/", views.get_staff, name="get_staff"),
    # /staff/new/
    path("staff/new/", views.new_staff, name="new_staff"),
]
