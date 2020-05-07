from django.urls import path

from .views import ProductDetailView, ProductListView, product_list_json, \
    product_detail_json

urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('api/', product_list_json, name='product_list_json'),
    path('api/product/<int:pk>/', product_detail_json, name='product_detail_json'),
]