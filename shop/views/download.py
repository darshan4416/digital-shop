from django.shortcuts import render, HttpResponse, redirect
from shop.models import Product

def downloadFree(request, product_id):
    try:
        product = Product.objects.get(id=product_id)
        if product.discount == 100:
            print("C'mon python")
            print(product.link)
            return redirect(product.file.url)
        else:
            return HttpResponse("<h1>Error coming from if</h1>")
    except:
        return HttpResponse("<h1>Error coming from try/except</h1>")







