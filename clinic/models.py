from django.db import models


class Speciality(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField()

    class Meta:
        verbose_name_plural = "Specialities"

    def __str__(self):
        return f"{self.name}"


class Doctor(models.Model):
    name = models.CharField(max_length=120)
    education = models.CharField(max_length=120, blank=True, null=True)
    speciality = models.ForeignKey(
        Speciality, related_name="doctors", on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.name}"


class Patient(models.Model):
    name = models.CharField(max_length=120)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    mobile_number = models.CharField(max_length=10)
    admitted_on = models.DateTimeField(auto_now_add=True)
    doctor = models.ForeignKey(
        Doctor,
        related_name="patients",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )

    def __str__(self):
        return f"{self.name}"


class Staff(models.Model):
    name = models.CharField(max_length=120)
    role = models.CharField(max_length=120)
    speciality = models.ForeignKey(
        Speciality,
        related_name="staffs",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )

    def __str__(self):
        return f"{self.name}"
