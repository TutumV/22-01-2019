from django.shortcuts import render, redirect
from django.views.generic import View
from .utils import *
from django.core.paginator import Paginator
from .models import User, Product, Category

# Create your views here.
def main_page(request):
    product = Product.objects.all()
    return render(request, 'app/main.html', context={'product', product})
