from django.shortcuts import render
from django.views.generic import DetailView, ListView

from django.http import JsonResponse

from .models import Product, Manufacturer

# Normal Django Views
class ProductDetailView(DetailView):
    model = Product
    
class ProductListView(ListView):
    model = Product


# JSON API Views
def product_list_json(request):
    products = Product.objects.all()
    data = {
        'products': list(products.values())
    }
    response = JsonResponse(data)
    return response

def product_detail_json(request, pk):
    try:
        product = Product.objects.get(pk=pk)
        data = {'product': 
            {
                'name': product.name,
                'manufacturer': product.manufacturer.name,
                'description': product.description,
                'photo': product.photo.url,
                'price': product.price,
                'shipping_cost': product.shipping_cost,
                'quantity': product.quantity,
            }
        }
        response = JsonResponse(data)
    except Product.DoesNotExist:
        response = JsonResponse(
            {
                'error': {
                    'code': 404,
                    'message': 'product not found',
                }
            },
            status=404
        )
    return response
