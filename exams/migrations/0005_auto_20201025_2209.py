# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-10-25 22:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0004_auto_20201025_2043'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exam',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='exam',
            name='time',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='question',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
