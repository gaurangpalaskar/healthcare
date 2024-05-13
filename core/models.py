from django.db import models


class Department(models.Model):
    dept_id = models.IntegerField(primary_key=True)
    dept_name = models.CharField(max_length=15)
    location = models.CharField(max_length=15)

