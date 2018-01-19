# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from datetime import datetime
from  django.contrib.auth.models import User
# Create your models here.


class Reload_country(models.Model):
    Country_Name = models.CharField(blank=False,max_length=100,default='')
    Country_short_name= models.CharField(blank=True,default='',max_length=100)
    Image = models.ImageField(blank=False,upload_to='media/')
    operators = models.ManyToManyField("Operator",blank=True)

    def __str__(self):
        return self.Country_Name

    class Meta:
        abstract = True
    class Meta:
        verbose_name = 'Reload Country'
        verbose_name_plural = ('Reload Country')

class Operator (models.Model):
    operator_name = models.CharField(blank=False,max_length=100,default='')
    code=models.CharField(blank=True,max_length=100,default='')
    products = models.ManyToManyField("Product", blank=True)
    def __str__(self):
        return self.operator_name


class Product (models.Model):
    Product_Amount=models.CharField(blank=True,default='',max_length=100)


    def __str__(self):
        return self.Product_Amount


# class Phone (models.Model):
#     Phone_No=models.CharField(blank=True,default='',max_length=100)
#     def __str__(self):
#         return self.Phone_No

class topup (models.Model):
    type = models.ManyToManyField("Operator",blank=True)
    amount= models.ManyToManyField("Product",blank=True)
    mobile= models.CharField(blank=True,max_length=100)
    time = models.DateTimeField(blank=True,default=datetime.now())
    ORDER_STATUS = ((0, 'Processing'), (1, 'Success'), (2, 'Failed'))
    status = models.SmallIntegerField(choices=ORDER_STATUS)

    class Meta:
     verbose_name = 'topup'
     verbose_name_plural = ('topup')

    def __str__(self):
     return self.mobile


