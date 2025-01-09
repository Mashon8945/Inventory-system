import json
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.views.decorators.csrf import csrf_exempt

from products.models import Products

# Create your views here.
@csrf_exempt
def list_products(request):
    if request.method == 'GET':
        products = list(Products.objects.values())
        return JsonResponse(products, safe=False)
    else:
        return JsonResponse(
            {
                'error' :'Method not allowed'
            },
            status = 405
        )

@csrf_exempt
def add_product(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        product = Products.objects.create(
            name = data['name'],
            description = data['description'],
            price = data['price'],
            stock = data['stock']
        )
        return JsonResponse(
            {
                'id': product.id,
                'message': 'Product added successfully'
            }
        )
    

@csrf_exempt
def update_product(request, product_id):
    if request.method == 'PUT':
        data = json.loads(request.body)
        product = get_object_or_404(Products, id = product_id)
        product.name = data.get('name', product.name)
        product.description = data.get('description', product.description)
        product.price = data.get('price', product.price)
        product.stock = data.get('stock', product.stock)
        product.save()
        return JsonResponse(
            {
                'message': 'Product updated successfully'
            }
        )

@csrf_exempt
def delete_product(request, product_id):
    if request.method == 'DELETE':
        product = get_object_or_404(Products, id = product_id)
        product.delete()
        return JsonResponse(
            {
                'message': 'Product deleted successfully'
            },
            status = 200
        )