from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    price = models.IntegerField(default=0)
    discount = models.IntegerField(default=0)
    active = models.BooleanField(default=True)
    file = models.FileField(upload_to='uploads/files', null=True, blank=True)
    thumbnail = models.ImageField(upload_to='uploads/thumbnails')
    fileSize = models.CharField(null=True, max_length=10)
    link = models.CharField(null=True, blank=True, max_length=100)

class ProductImages(models.Model):
    product = models.ForeignKey(Product, default=None, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='uploads/images', blank=True)



