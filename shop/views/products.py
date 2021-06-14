from django.views import View
from django.shortcuts import redirect, render
from shop.models import User, Product, ProductImages


def productDetails(request, product_id):
    product = Product.objects.get(id=product_id)
    images = ProductImages.objects.filter(product = product.id)
    return render(request, 'product_details.html', context={'product': product, 'images': images})
