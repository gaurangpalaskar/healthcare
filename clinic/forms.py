from django import forms

from .models import Speciality, Doctor, Patient, Staff


class SpecialityForm(forms.ModelForm):
    description = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "rows": 10,
                "placeholder": "What's this new speciality is all about?",
            }
        ),
        max_length=5000,
        help_text="The maximum length of the description is 5000",
    )

    class Meta:
        model = Speciality
        fields = ["name", "description"]


class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ["name", "education", "speciality"]


class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ["name", "age", "gender", "mobile_number", "doctor"]


class StaffForm(forms.ModelForm):
    class Meta:
        model = Staff
        fields = ["name", "role", "speciality"]
