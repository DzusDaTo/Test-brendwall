from django.urls import path
from .views import product_form, product_list, create_product, list_products

urlpatterns = [
    path('add-product/', product_form, name='product_form'),
    path('view-products/', product_list, name='product_list'),
    path('api/products/create/', create_product, name='create_product'),
    path('api/products/', list_products, name='list_products'),
]