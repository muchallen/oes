# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-10-21 02:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0003_correctsolution_question_solutionstext'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='correctsolution',
            name='correct_solution',
        ),
        migrations.AddField(
            model_name='correctsolution',
            name='correct_solution_letter',
            field=models.CharField(default=1, max_length=1),
            preserve_default=False,
        ),
    ]