# Generated by Django 2.0 on 2019-12-07 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('EmpName', models.CharField(max_length=100)),
                ('EmpId', models.CharField(max_length=30, unique=True)),
            ],
        ),
    ]
