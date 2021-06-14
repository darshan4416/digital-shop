from django.contrib import admin
from .models.product import Product, ProductImages
from .models.user import User
from django.utils.html import format_html
from .models.payment import Payment

# Register your models here.
class ProductImagesModel(admin.StackedInline):
    model = ProductImages


class ProductModel(admin.ModelAdmin):
    list_display = ['id', 'name', 'get_description', 'get_price', 'get_discount', 'get_salePrice',
                    'file', 'thumbnail']
    inlines = [ProductImagesModel]

    def get_description(self, obj):
        return format_html(f'<span title="{obj.description}">{obj.description[0:15]}..</span>')

    def get_price(self, obj):
        return '₹' + str(obj.price)

    def get_discount(self, obj):
        return str(obj.discount) + ' %'

    def get_salePrice(self, obj):
        return '₹' + str(obj.price - obj.price * (obj.discount / 100))

    get_price.short_description = 'Price'
    get_discount.short_description = 'Discount'
    get_salePrice.short_description = 'Sale Price'
    get_description.short_description = 'Description'

class UserModel(admin.ModelAdmin):
    list_display = ['email']

admin.site.register(Product, ProductModel)
admin.site.register(User, UserModel)
admin.site.register(Payment)
