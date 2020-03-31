from django.http.response import JsonResponse

from core.models import Category
from core.models import Product

def product_list(request):
    products = Product.objects.all()
    products_json = [product.to_json() for product in products]
    return JsonResponse(products_json, safe=False)

def product_details(request, product_id):
    try:
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist as e:
        return JsonResponse({'Error': str(e)})
    return JsonResponse(product.to_json())

def categories_list(request):
    categories = Category.objects.all()
    json_categories = [c.to_json() for c in categories]
    return JsonResponse(json_categories, safe=False)


def category_detail(request, category_id):
    try:
        category = Category.objects.get(id=category_id)
    except Category.DoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False)

    return JsonResponse(category.to_json())

def products_of_category(request, category_id):
    try:
        category = Category.objects.get(id=category_id)
    except Category.DoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False)

    products = category.product_set.all()
    json_products = [p.to_json() for p in products]
    return JsonResponse(json_products, safe=False)