# Generated by Django 5.0.4 on 2024-05-13 14:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employees',
            fields=[
                ('emp_id', models.IntegerField(primary_key=True, serialize=False)),
                ('emp_name', models.CharField(max_length=20)),
                ('job', models.CharField(max_length=10)),
                ('manager_id', models.IntegerField()),
                ('hire_date', models.DateTimeField()),
                ('salary', models.IntegerField()),
                ('comm', models.IntegerField(default=0, null=True)),
                ('dept_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.department')),
            ],
        ),
    ]
