# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from companies import models as companymodels

# Create your models here.
class Testee(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    id_number = models.CharField(max_length=200)
    email=models.EmailField(max_length=254)
    company=models.ForeignKey(companymodels.Company,default="None")