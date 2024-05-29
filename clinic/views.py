from django.shortcuts import render, redirect

from .forms import SpecialityForm, DoctorForm, PatientForm, StaffForm
from .models import Speciality, Doctor, Patient, Staff


def dashboard(request):
    return render(request, "clinic\dashboard.html")


def get_specialities(request):
    specialities = Speciality.objects.all().order_by("name")
    context = {"specialities": specialities}
    return render(request, "clinic\specialities.html", context)


def get_speciality(request, id):
    speciality = Speciality.objects.get(id=id)
    doctors = speciality.doctors.all().order_by("name")
    staffs = speciality.staffs.all().order_by("name")
    context = {"speciality": speciality, "doctors": doctors, "staffs": staffs}
    return render(request, "clinic\speciality.html", context)


def new_speciality(request):
    if request.method == "POST":
        form = SpecialityForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("clinic:specialities")

    else:
        form = SpecialityForm()

    return render(request, "clinic\\new_speciality.html", {"form": form})


def get_doctors(request):
    doctors = Doctor.objects.all().order_by("name")
    context = {"doctors": doctors}
    return render(request, "clinic\doctors.html", context)


def get_doctor(request, id):
    doctor = Doctor.objects.get(id=id)
    patients = doctor.patients.all().order_by("name")
    context = {"doctor": doctor, "patients": patients}
    return render(request, "clinic\doctor.html", context)


def new_doctor(request):
    if request.method == "POST":
        form = DoctorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("clinic:doctors")

    else:
        form = DoctorForm()

    return render(request, "clinic\\new_doctor.html", {"form": form})


def get_patients(request):
    patients = Patient.objects.all().order_by("name")
    context = {"patients": patients}
    return render(request, "clinic\patients.html", context)


def get_patient(request, id):
    patient = Patient.objects.get(id=id)
    context = {"patient": patient}
    return render(request, "clinic\patient.html", context)


def new_patient(request):
    if request.method == "POST":
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("clinic:patients")

    else:
        form = PatientForm()

    return render(request, "clinic\\new_patient.html", {"form": form})


def get_staffs(request):
    staffs = Staff.objects.all().order_by("name")
    context = {"staffs": staffs}
    return render(request, "clinic\staffs.html", context)


def get_staff(request, id):
    staff = Staff.objects.get(id=id)
    context = {"staff": staff}
    return render(request, "clinic\staff.html", context)


def new_staff(request):
    if request.method == "POST":
        form = StaffForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("clinic:staffs")

    else:
        form = StaffForm()

    return render(request, "clinic\\new_staff.html", {"form": form})
