from django.urls import path
from .views import *

urlpatterns = [
    path('', main_page, name='main_page_url'),
    path('register/', register, name='register_url'),
    path('login/', login, name='login_url')
#   path('category/' category_list, name='category_list_url'),
#   path('category/<str:slug>/', CategoryList.as_view(), name='category_detail_url'),
#   path('order/', OrderList.as_view(), name='order_list_url'),
#   path('delivery/', delivery_page, name='delivery_page_url'),
#   path('compare/<str:slug>/', ComparePage.as_view(), name='compare_page_url'),
#   path('product/create/', ProductCreate.as_view(),name='product_create_url'),
#   path('product/<str:slug>/'. ProductDetail.as_view(), name='product_detail_url'),
#   path('product/<str:slug>/update', ProductUpdate.as_view(), name='product_update_url'),
#   path('product/<str:slug>/delete', ProductDelete.as_view(, name='product_delete_url'),
#   path('category/create/', CategoryCreate.as_view(), name='category_create_url'),
#   path('category/<str:slug>/delete', CategoryDelete.as_view(), name='category_delete_url'),
#   path('profile/', user_profile, name='user_profile_url'),
#   path('profile/personal-info', personal_info, name='personal_info_url')
]