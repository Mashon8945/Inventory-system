from django.urls import path
from .views import list_products, add_product, update_product, delete_product

urlpatterns = [
    path('products/', list_products, name='list_products'),
    path('products/add/', add_product, name='add_product'),
    path('products/update/<int:product_id>/', update_product, name='add_product'),
    path('products/delete/<int:product_int>/', delete_product, name='delete_product'),
]