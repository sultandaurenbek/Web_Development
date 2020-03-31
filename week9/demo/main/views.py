from django.http.response import HttpResponse, JsonResponse
from django.http.request import HttpRequest

# Create your views here.
def hello(request):
    return HttpResponse('<h1>Welcome to my first Shop</h1>')

products = []
for i in range(1,5):
    products.append(
        {
            'id': i,
            'name': f'products {i}',
            'price': i*1000
        }
    )

def product_list(request):
    return JsonResponse(products, safe=False)

def product_details(request, product_id):
    for product in products:
        if product['id'] == product_id:
            return JsonResponse(product)
    return JsonResponse({'Error': 'product does not exists'})
