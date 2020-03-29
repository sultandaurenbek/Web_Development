from django.urls import path
from api import views

urlpatterns = [
    path('categories/', views.category_list),
    path('categories/<int:category_id>', views.category_one),
    path('products/', views.product_list),
    path('products/<int:product_id>', views.product_one),
    path('categories/<int:category_id>/products', views.product_list_by_category_id)
]