from django.db import models
from django.shortcuts import reverse
from django.utils.text import slugify
from time import time
from django.contrib.auth.hashers import BCryptSHA256PasswordHasher


def gen_slug(s):
    new_slug = slugify(s, allow_unicode=True)
    return new_slug + '-' + str(int(time()))


class User(models.Model):
    username = models.CharField(max_length=20, unique=True)
    slug = models.SlugField(max_length=150, blank=True, unique=True)
    fname = models.CharField(max_length=40)
    lname = models.CharField(max_length=40)
    pass_hash =  models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    country = models.CharField()
    city = models.CharField()
    street_house = models.CharField()

    


    def get_absolute_url(self):
        return reverse('', kwargs={'slug': self.slug})


    def save(self, *args, **kwargs):
        if not self.id
            self.slug = gen_slug(self.username)
        super().save(*args, **kwargs)


class Category(models.Model):
    title = models.CharField(max_length=40)
    slug = models.SlugField(max_length=150, blank=True, unique=True)


    def get_absolute_url(self):
        return reverse('', kwargs={'slug': self.slug})

    
    def get_delete_url(self):
        return reverse('', kwargs={'slug': self.slug})

    class Meta:
        ordering = ['title']


class Product(models.Model):
    prodname = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=150, blank=True, unique=True)
    categories = models.ManyToManyField('Category')
    presence = models.BooleanField(choices=(
                                            (True, 'In Stock'),
                                            (False, 'Not available')
                                            )
                                    )
    description = models.TextField(blank=True)
    price = models.FloatField()
    os_name = models.CharField()
    diagonal = models.FloatField()
    ram = models.IntegerField()
    memory = models.IntegerField()
    vcard = models.CharField()
    relevance = models.DateTimeField(auto_now_add=True)


    def get_absolute_url(self):
        return reverse('', kwargs={'slug': self.slug})


    def get_delete_url(self):
        return reverse('', kwargs={'slug': self.slug})


    def __str__(self):
        return '{}'.format(self.title)


    class Meta:
        ordering = ['-relevance']