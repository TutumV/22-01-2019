from django.urls import path
from .views import *

urlpatterns = [
    path('', main_page, name='main_page_url'),
    path('category/create/', CategoryCreate.as_view(), name='category_create_url'),
    path('category/', category_list, name='category_list_url'),
    path('category/<str:slug>/', CategoryDetail.as_view(), name='category_detail_url'),
    path('category/<str:slug>/delete/', CategoryDelete.as_view(), name='category_delete_url'),
    path('product/create/', ProductCreate.as_view(),name='product_create_url'),
    path('product/<str:slug>/', ProductDetail.as_view(), name='product_detail_url'),
    path('product/<str:slug>/update/', ProductUpdate.as_view(), name='product_update_url'),
    path('product/<str:slug>/delete/', ProductDelete.as_view(), name='product_delete_url'),
    path('delivery/', delivery_base, name='delivery_base_url'),
    path('delivery/<str:slug>/create', DeliveryCreate.as_view(), name='delivery_create_url'),
    path('delivery/<str:slug>/', DeliveryDetail.as_view(), name='delivery_detail_url'),
    path('delivery/<str:slug>/delete/', DeliveryDelete.as_view(), name='delivery_delete_url'),
    path('shop/', shop_base, name='shop_base_url'),
    path('shop/create', ShopCreate.as_view(), name='shop_create_url'),
    path('shop/<str:slug>/', ShopDetail.as_view(), name='shop_detail_url'),
    path('shop/<str:slug>/delete/', ShopDelete.as_view(), name='shop_delete_url')
]