from django.contrib import admin

# Register your models here.
from shop.models import Product,Shop,Category

admin.site.register(Product)
admin.site.register(Shop)
admin.site.register(Category)