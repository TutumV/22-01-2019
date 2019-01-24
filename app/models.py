from django.db import models
from django.shortcuts import reverse
from django.utils.text import slugify
from time import time


def gen_slug(s):
    new_slug = slugify(s, allow_unicode=True)
    return new_slug + '-' + str(int(time()))


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
    vcard = models.CharField(max_length=100)
    relevance = models.DateTimeField(auto_now_add=True)


    def get_absolute_url(self):
        return reverse('product_detail_url', kwargs={'slug': self.slug})

    def get_update_url(self):
        return reverse('product_update_url', kwargs={'slug': self.slug})

    def get_delete_url(self):
        return reverse('product_delete_url', kwargs={'slug': self.slug})


    def __str__(self):
        return '{}'.format(self.prodname)


    class Meta:
        ordering = ['-relevance']