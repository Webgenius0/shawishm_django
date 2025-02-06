# Generated by Django 5.1.4 on 2025-01-13 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='RG_ID',
            field=models.CharField(blank=True, db_column='RG_ID', max_length=45, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='U_Role',
            field=models.CharField(blank=True, db_column='U_Role', max_length=45, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='U_address',
            field=models.CharField(blank=True, db_column='U_Address', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='U_fullname',
            field=models.CharField(blank=True, db_column='U_FullName', max_length=45, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='U_phone',
            field=models.CharField(blank=True, db_column='U_Phone', max_length=45, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='U_sex',
            field=models.CharField(blank=True, db_column='U_Sex', max_length=45, null=True),
        ),
    ]
