from django.shortcuts import render, redirect
from django.views.generic import View
from .utils import *
from django.core.paginator import Paginator
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import  Product, Category, Delivery, Shop
from .forms import CategoryForm, ProductForm, DeliveryForm, ShopForm
from django.db.models import Q



def main_page(request):
    search_query = request.GET.get('search', '')

    if search_query:
        product = Product.objects.filter(prodname__icontains=search_query)
    else:
        product = Product.objects.all()

    paginator = Paginator(product, 4)

    page_number = request.GET.get('page', 1)
    page = paginator.get_page(page_number)

    is_paginated = page.has_other_pages()

    if page.has_previous():
        prev_url = '?page={}'.format(page.previous_page_number())
    else:
        prev_url = ''

    if page.has_next():
        next_url = '?page={}'.format(page.next_page_number())
    else:
        next_url = ''

    context = {
        'page_object': page,
        'is_paginated': is_paginated,
        'next_url': next_url,
        'prev_url': prev_url
    }


    return render(request, 'app/index.html', context=context)


class ProductDetail(ObjectDetailMixin, View):
    model = Product
    template = 'app/product_detail.html'


class ProductCreate(LoginRequiredMixin, ObjectCreateMixin, View):
    model_form = ProductForm
    template = 'app/product_create.html'
    raise_exception = True


class ProductUpdate(LoginRequiredMixin, ObjectUpdateMixin, View):
    model = Product
    model_form = ProductForm
    template = 'app/product_update.html'
    raise_exception = True


class ProductDelete(LoginRequiredMixin, ObjectDeleteMixin, View):
    model = Product
    template = 'app/product_delete.html'
    redirect_url = 'main_page_url'
    raise_exception = True


class CategoryDetail(ObjectDetailMixin, View):
    model = Category
    template = 'app/category_detail.html'


class CategoryCreate(LoginRequiredMixin, ObjectCreateMixin, View):
    model_form = CategoryForm
    template = 'app/category_create.html'
    raise_exception = True


class CategoryDelete(LoginRequiredMixin, ObjectDeleteMixin, View):
    model = Category
    template = 'app/category_delete.html'
    redirect_url = 'category_list_url'
    raise_exception = True


class DeliveryCreate(ObjectCreateMixin,View):
    model_form = DeliveryForm
    template = 'app/delivery_create.html'


class DeliveryDetail(ObjectDetailMixin, View):
    model = Delivery
    template = 'app/delivery_detail.html'

class DeliveryDelete(LoginRequiredMixin, ObjectDeleteMixin, View):
    model = Delivery
    template = 'app/delivery_delete.html'
    redirect_url = 'delivery_base_url'
    raise_exception = True


class ShopCreate(LoginRequiredMixin, ObjectCreateMixin,View):
    model_form = ShopForm
    template = 'app/shop_create.html' 
    raise_exception = True


class ShopDetail(ObjectDetailMixin, View):
    model = Shop
    template = 'app/shop_detail.html'


class ShopDelete(LoginRequiredMixin, ObjectDeleteMixin, View):
    model = Shop
    template = 'app/shop_delete.html'
    redirect_url = 'shop_base_url'
    raise_exception = True



def category_list(request):
    categories = Category.objects.all()
    return render(request, 'app/category_list.html', context={'categories': categories})


def delivery_base(request):
    delivery = Delivery.objects.all()
    return render(request, 'app/delivery_base.html', context={'delivery': delivery})
    
def shop_base(request):
    bshop = Shop.objects.all()
    return render(request, 'app/shop_base.html',context={'bshop': bshop})