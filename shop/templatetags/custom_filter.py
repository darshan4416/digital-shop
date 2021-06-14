from django import template

register = template.Library()

@register.filter(name='rupee')
def addRuppeeSign(value):
    return f'₹{value}';

@register.filter(name='sale_price')
def getsaleprice(product):
    return product.price - (product.discount * product.price)/100;