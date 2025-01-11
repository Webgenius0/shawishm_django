# Generated by Django 5.1.4 on 2025-01-11 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RadiologyGroup',
            fields=[
                ('Rg_Inc_ID', models.BigAutoField(db_column='RG_Inc_ID', editable=False, primary_key=True, serialize=False, unique=True)),
                ('Rg_ID', models.IntegerField(blank=True, db_column='RG_ID', null=True)),
                ('Rg_Name', models.CharField(blank=True, db_column='RG_Name', max_length=45, null=True)),
                ('Rg_Members', models.CharField(blank=True, db_column='RG_Members', max_length=100, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
