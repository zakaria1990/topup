# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from topup_projects.models import Reload_country,Operator,Product,topup

# Register your models here.
admin.site.register(Reload_country)
admin.site.register(Operator)
admin.site.register(Product)
admin.site.register(topup)
# admin.site.register(Phone)
