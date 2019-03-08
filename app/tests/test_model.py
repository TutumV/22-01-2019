from django.test import TestCase
from app.models import Category, Shop, Product, Delivery
from django.test import Client
from time import time

class CategoryTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_category_create(self):
        Category.objects.create(title='zxc', slug='zxc')
        response = self.client.get('/category/')
        response_category = self.client.get('/category/zxc/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response_category.status_code, 200)


    def test_category_list(self):
        Category.objects.create(title='zxc', slug='zxc')
        category_list = Category.objects.all().count()
        self.assertEqual(category_list, 1)


    def test_category_delete(self):
        Category.objects.create(title='zxc', slug='zxc')
        Category.objects.all().delete()
        self.assertEqual(Category.objects.all().count(), 0)

class ShopTestCase(TestCase):


    def test_shop_create(self):
        Shop.objects.create(slug='zxc', address='abc', country='ru', city='spb', work_time='1-2', time_delivery='3')
        response = self.client.get('/shop/')
        response_shop = self.client.get('/shop/abc%20spb/')
        shop_list = Shop.objects.all().count()
        self.assertEqual(response_shop.status_code, 200)
        self.assertEqual(shop_list, 1)


    def test_shop_update(self):
        Shop.objects.create(slug='zxc', address='abc', country='ru', city='spb', work_time='1-2', time_delivery='3')
        Shop.objects.filter(address='abc').update(slug='xzc')
        old_response_shop = self.client.get('/shop/zxc/')
        new_response_shop = self.client.get('/shop/xzc/')
        undefiend = self.client.get('/shop/sadadsada2w123/')
        self.assertEqual(undefiend.status_code, 404)
        self.assertEqual(old_response_shop.status_code, 404)
        self.assertEqual(new_response_shop.status_code, 200)


    def test_shop_delete(self):
        Shop.objects.create(slug='zxc', address='abc', country='ru', city='spb', work_time='1-2', time_delivery='3')
        shop_list = Shop.objects.all().delete()
        self.assertEqual(Shop.objects.all().count(), 0)


class ProductTestCase(TestCase):


    def test_product_create(self):
        category_1 = Category.objects.create(title='zxc', slug='zxc')
        product_1 = Product.objects.create(prodname='Phone', slug='Phone123', presence=True, description='zxc', \
                                           price='123', os_name='macOS', diagonal='23', ram='2', memory='16', videocard='nvidia123', \
                                           )
        product_1.categories.add(category_1)
        response = self.client.get('/')
        response_product = self.client.get(Product.objects.all()[0].get_absolute_url())
        product_list = Product.objects.all()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response_product.status_code, 200)


    def test_product_update(self):
        pass


    def test_product_delete(self):
        pass


class DeliveryTestCase(TestCase):


    def test_delivery_create(self):
        pass


    def test_delivery_delete(self):
        pass
