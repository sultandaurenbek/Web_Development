from django.urls import path

from core.views import product_list, product_details, categories_list, category_detail, products_of_category

urlpatterns = [
    path('products/', product_list),
    path('products/<int:product_id>/', product_details),
    path('categories/', categories_list),
    path('categories/<int:category_id>/', category_detail),
    path('categories/<int:category_id>/products/', products_of_category),
]