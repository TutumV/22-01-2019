from django import forms
from .models import Category, Product, Shop, Delivery
from django.core.exceptions import ValidationError



class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['title', 'slug']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def clean_slug(self):
        new_slug = self.cleaned_data['slug'].lower()

        if new_slug == 'create':
            raise ValidationError('Slug may not be "Create"')
        if Category.objects.filter(slug__iexact=new_slug).count():
            raise ValidationError('Slug must be unique. We have "{}" slug already'.format(new_slug))
        return new_slug


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['prodname', 'slug', 'categories', 'presence', \
        'description', 'price', 'os_name', 'diagonal', 'ram', 'memory', 'videocard']

        widgets = {
            'prodname': forms.TextInput(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
            'categories': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'price': forms.TextInput(attrs={'class': 'form-control'}),
            'os_name': forms.TextInput(attrs={'class': 'form-control'}),
            'diagonal': forms.NumberInput(attrs={'class': 'form-control'}),
            'ram': forms.NumberInput(attrs={'class': 'form-control'}),
            'memory': forms.NumberInput(attrs={'class': 'form-control'}),
            'videocard': forms.TextInput(attrs={'class': 'form-control'})
        }


    def clean_slug(self):
        new_slug = self.cleaned_data['slug'].lower()

        if new_slug == 'create':
            raise ValidationError('Slug may not be "Create"')
        return new_slug


class DeliveryForm(forms.ModelForm):
    class Meta:
        model = Delivery
        fields = ['shops', 'delivery_product']

        widgets = {
            'shops': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'delivery_product': forms.SelectMultiple(attrs={'class': 'form-control'})
        }

class ShopForm(forms.ModelForm):
    class Meta:
        model = Shop
        fields = ['address', 'country', 'city', 'work_time', 'time_delivery']

        widgets = {
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'country': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'work_time': forms.TextInput(attrs={'class': 'form-control'}),
            'time_delivery': forms.NumberInput(attrs={'class': 'form-control'})
        }
