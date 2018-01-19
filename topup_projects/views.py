# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect,HttpResponse
from .models import Reload_country, Operator,Product,topup
from  django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect
from  django.contrib import auth
# import  requests
# Create your views here.

# def user(request):


def login(request):
    if request.method == "POST":
        user = request.POST.get('user')
        password = request.POST.get('password')
        use = authenticate(request,username=user, password=password)

        if use is not None:
            auth.login(request,use)
            return redirect('details_page')


    context = {'Reload_country': Reload_country.objects.all(),}



    return render(request,'topup_projects/login.html', context)


def home(request):
    context = {'Reload_country': Reload_country.objects.all(),}

    return render(request,'topup_projects/login.html', context)

def test(request):
    context = {'Reload_countrys':Reload_country.objects.all(),'Operator_li':Operator.objects.all(),
           }

    return render(request,'topup_projects/details_page.html', context)


def select_country(request,id):
    if request.POST:
        product=Product.objects.get(id=request.POST.get("product_data"))
        operator=Operator.objects.get(id=request.POST.get("oprator_data"))
        mobile_number=request.POST.get("mobile_data")
        topup_object=topup.objects.create(mobile=mobile_number,status=0)
        # type = operator, amount = product,
        topup_object.type.add(operator)
        topup_object.amount.add(product)
        topup_object.save()

    # print Reload_country.objects.get(id)
    context = {'Reload_countrys':Reload_country.objects.all(), 'Reload_country': Reload_country.objects.filter(id=id),
               'Operator_li': Operator.objects.all(),
               'products': Product.objects.all(),
               'topup':topup.objects.all(),

               }

    return render(request, 'topup_projects/details_page.html', context)

def filter_purchase_product(request):
    products = Product.objects.all()
    if request.POST:
        selected_product = products.objects.get(id=request.POST.get("selected_product"))
        select_operator=Operator.objects.all()
        for puchase in select_operator:
            for p in puchase.products.all():
                selected_product.append((p))
                continue

    context= {'Operator_li': Operator.objects.all(),'products': Product.objects.all()}

    return render(request, 'topup_projects/details_page.html', context)


# def CallApi(request):
#     url = 'http://52.76.43.186/Catalog/AndroidCategoryProducts'
#     params = {'pagenumber':'1','categoryId':'1','orderBy':'','priceRange':'0-100000','BrandRange':''}
#     r = requests.get(url,params)
#     books = r.json()
#     return HttpResponse(books)
