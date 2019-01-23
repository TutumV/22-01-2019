from django.shortcuts import render, redirect
from django.views.generic import View
from .utils import *
from django.core.paginator import Paginator
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import  Product, Category
from .forms import CategoryForm, ProductForm
from django.db.models import Q



def main_page(request):
    search_query = request.GET.get('search', '')

    if search_query:
        product = Product.objects.filter(prodname__icontains=search_query)
    else:
        product = Product.objects.all()

    paginator = Paginator(product, 10)

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


def category_list(request):
    category = Category.objects.all()
    return render(request, 'app/category_list.html', context={'category': category})