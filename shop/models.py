from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.name

class Shop(models.Model):
    name = models.CharField(max_length=300)
    Address = models.TextField()
    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=300)
    quantity = models.IntegerField()
    price = models.FloatField()
    image = models.ImageField()
    description = models.TextField()
    category = models.ForeignKey(Category)
    seller = models.ForeignKey(Shop)
    ## seller
    def __str__(self):
        return self.name





    #shop_name = models.CharField(max_length=300)
