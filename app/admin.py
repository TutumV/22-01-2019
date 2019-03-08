from django.contrib import admin
from .models import Product, Delivery, Shop, Category
# Register your models here.


admin.site.register(Product)
admin.site.register(Delivery)
admin.site.register(Shop)
admin.site.register(Category)
