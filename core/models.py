from django.db import models


class Department(models.Model):
    dept_id = models.IntegerField(primary_key=True)
    dept_name = models.CharField(max_length=15)
    location = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.dept_name}"

class Employees(models.Model):
    emp_id = models.IntegerField(primary_key=True)
    emp_name = models.CharField(max_length=20)
    job = models.CharField(max_length=10)
    manager_id = models.IntegerField()
    hire_date = models.DateTimeField()
    salary = models.IntegerField()
    comm = models.IntegerField(null=True, default=0)
    dept_id = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.emp_name}"