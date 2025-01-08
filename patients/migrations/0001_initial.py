# Generated by Django 5.1.4 on 2025-01-08 09:46

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Patients',
            fields=[
                ('patients_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('pat_inc_id', models.PositiveBigIntegerField(db_column='Pat_inc_id', unique=True)),
                ('pat_inc_id_string', models.CharField(blank=True, db_column='Pat_inc_id_string', max_length=50, null=True)),
                ('pat_id', models.CharField(blank=True, db_column='Pat_id', max_length=50, null=True)),
                ('pat_name', models.CharField(blank=True, db_column='Pat_name', max_length=70, null=True)),
                ('pat_sex', models.CharField(blank=True, db_column='Pat_sex', max_length=10, null=True)),
                ('pat_dob', models.DateField(blank=True, db_column='Pat_DOB', null=True)),
                ('pat_phone', models.CharField(blank=True, db_column='Pat_phone', max_length=25, null=True)),
                ('notes', models.TextField(blank=True, db_column='Notes', null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
