from django.db import  models
from .category import Category

class Product(models.Model):
    name= models.CharField(max_length =50)
    price = models.IntegerField(default =0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,default=1)
    description = models.CharField(max_length=200, default='', null= True, blank= True)
    image = models.ImageField(upload_to='products/')

    @staticmethod

    def get_all_products():         # get product from database
        return Product.objects.all()


    @staticmethod
    def get_all_products_by_Categoryid(categort_id):
        if categort_id:
            return Product.objects.filter(category= categort_id)
        else:
            return  Product.get_all_products()