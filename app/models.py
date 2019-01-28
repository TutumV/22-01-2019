from django.db import models
from django.shortcuts import reverse
from django.utils.text import slugify
from time import time
from uuid import uuid4


def gen_slug(s):
    new_slug = slugify(s, allow_unicode=True)
    return new_slug + '-' + str(int(time()))


def generateUUID():
    return str(uuid4())


class Category(models.Model):
    title = models.CharField(max_length=40)
    slug = models.SlugField(max_length=150, blank=True, unique=True)


    def get_absolute_url(self):
        return reverse('category_detail_url', kwargs={'slug': self.slug})

    
    def get_delete_url(self):
        return reverse('category_delete_url', kwargs={'slug': self.slug})

    
    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']


class Product(models.Model):
    prodname = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=150, blank=True, unique=True)
    categories = models.ManyToManyField('Category', related_name='products')
    presence = models.BooleanField(default=False)
    description = models.TextField(blank=True)
    price = models.FloatField()
    os_name = models.CharField(max_length=50)
    diagonal = models.FloatField()
    ram = models.IntegerField()
    memory = models.IntegerField()
    videocard = models.CharField(max_length=100)
    relevance = models.DateTimeField(auto_now_add=True)


    def get_absolute_url(self):
        return reverse('product_detail_url', kwargs={'slug': self.slug})

    def get_update_url(self):
        return reverse('product_update_url', kwargs={'slug': self.slug})

    def get_delete_url(self):
        return reverse('product_delete_url', kwargs={'slug': self.slug})

    
    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = gen_slug(self.prodname)
        super().save(*args, **kwargs)


    def __str__(self):
        return '{}'.format(self.prodname)


    class Meta:
        ordering = ['-relevance']


class Delivery(models.Model):
    slug = models.CharField(default=generateUUID, max_length=36, unique=True, editable=False)
    shops = models.ManyToManyField('Shop', related_name='deliveries')
    delivery_product = models.ManyToManyField('Product', related_name='orders')
    delivery_relevance = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('delivery_detail_url', kwargs={'slug': self.slug})

    def get_delete_url(self):
        return reverse('delivery_delete_url', kwargs={'slug': self.slug})


    def __str__(self):
        return '{}'.format(self.slug)


    class Meta:
        ordering = ['delivery_relevance']

class Shop(models.Model):
    slug = models.SlugField(max_length=150, blank=True, unique=True)
    address = models.CharField(max_length=150)
    country = models.CharField(max_length=150)
    city = models.CharField(max_length=150)
    work_time = models.CharField(max_length=100)
    time_delivery = models.IntegerField()

    def get_absolute_url(self):
        return reverse('shop_detail_url', kwargs={'slug': self.slug})

    
    def get_delete_url(self):
        return reverse('shop_delete_url', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = self.address + ' ' + self.city
        super().save(*args, **kwargs)


    def __str__(self):
        return self.address

