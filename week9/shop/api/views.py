from django.shortcuts import render
from django.http.response import JsonResponse
from api.models import Category
from api.models import Product

# Create your views here.

def category_list(request):
    categories = Category.objects.all()
    json_categories = [c.to_json() for c in categories]
    return JsonResponse(json_categories, safe=False)

def product_list(request):
    products = Product.objects.all()
    json_products = [p.to_json() for p in products]
    return JsonResponse(json_products, safe=False)

def category_one(request, category_id):
    try:
        category = Category.objects.get(id=category_id)
    except Category.DoesNotExist as e:
        return JsonResponse({'error': str(e)})
    return JsonResponse(category.to_json())

def product_one(request, product_id):
    try:
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist as e:
        return JsonResponse({'error': str(e)})
    return JsonResponse(product.to_json())

def product_list_by_category_id(request, category_id):
    c = Category.objects.get(id=category_id)
    products = Product.objects.filter(category=c)
    json_products = [p.to_json() for p in products]
    return JsonResponse(json_products, safe=False)
