# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Company(models.Model):
    company_name=models.CharField(max_length=500)
    staff_name=models.CharField(max_length=200)
    staff_number= models.CharField(max_length=200)

    def __str__(self):
        return self.company_name



