from django.shortcuts import render
from shop.models import Shop,Product,Category
# Create your views here.
def index(request):
    shops = Shop.objects.all()
    print(shops)

    return render(request,"index.html",{"shops":shops})

def shop(request,id):
    shop = Shop.objects.get(pk=id)
    products= Product.objects.filter(seller=shop)
    return render(request,"shop.html",{"products":products})

def product(request,id):
    product = Product.objects.get(pk=id)
    return render(request,"product.html",{"product":product})