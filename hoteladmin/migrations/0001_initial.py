# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-09-28 11:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AdminModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hotelname', models.CharField(max_length=300)),
                ('address', models.CharField(max_length=100)),
                ('mobilenumber', models.CharField(max_length=100)),
                ('roomcategory', models.CharField(max_length=100)),
                ('actype', models.CharField(max_length=100)),
                ('uploadimage', models.ImageField(upload_to='')),
            ],
        ),
    ]
