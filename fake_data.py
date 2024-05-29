import os
import django
import random

from faker import Faker

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "website.settings")
django.setup()

from clinic.models import Speciality, Doctor, Patient, Staff

fake = Faker()


specialities_data = [
    {
        "name": "Physiotherapy",
        "description": "Department focusing on physical therapy treatments",
    },
    {
        "name": "Obstetrics",
        "description": "Department specializing in childbirth and care of pregnant women",
    },
    {
        "name": "Gynecology",
        "description": "Department dealing with health of the female reproductive systems",
    },
    {
        "name": "Orthopedics",
        "description": "Department focused on the musculoskeletal system",
    },
    {
        "name": "Neurology",
        "description": "Department dealing with disorders of the nervous system",
    },
    {
        "name": "Dermatology",
        "description": "Department focusing on skin, hair, and nail conditions",
    },
    {
        "name": "Paediatrics",
        "description": "Department dedicated to the medical care of infants, children, and adolescents",
    },
    {
        "name": "Cardiology",
        "description": "Department specializing in heart and cardiovascular diseases",
    },
    {
        "name": "Oncology",
        "description": "Department dealing with the prevention, diagnosis, and treatment of cancer",
    },
    {
        "name": "Radiology",
        "description": "Department focusing on medical imaging to diagnose and treat diseases",
    },
]

# Create 10 specialities
specialities = []
for item in specialities_data:
    name = item["name"]
    description = item["description"]
    speciality = Speciality.objects.create(name=name, description=description)
    specialities.append(speciality)

# Create 5 doctors for each speciality
for speciality in specialities:
    for _ in range(5):
        name = f"{fake.name()}"
        education = fake.text(max_nb_chars=20)
        doctor = Doctor.objects.create(
            name=name, education=education, speciality=speciality
        )

        # Create 10 patients for each doctor
        for _ in range(10):
            patient_name = fake.name()
            age = random.randint(1, 100)
            gender = random.choice(["Male", "Female"])
            mobile_number = fake.random_number(digits=10, fix_len=True)
            Patient.objects.create(
                name=patient_name,
                age=age,
                gender=gender,
                mobile_number=str(mobile_number),
                doctor=doctor,
            )

    # Create 5 staff members for each speciality
    for _ in range(5):
        staff_name = fake.name()
        role = fake.job()
        Staff.objects.create(name=staff_name, role=role, speciality=speciality)

print("Data population complete!")
