# Generated by Django 2.1.5 on 2019-12-15 17:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('calen', '0003_vacations'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Vacations',
            new_name='Vacation',
        ),
    ]