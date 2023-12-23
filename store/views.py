from django.shortcuts import render
from django.http import HttpResponse
from .models.product import Product
from .models.category import Category


#Create your view here
def index(request):
    products = None
    categories= Category.get_all_Categories()  # get all categiries from category class
    categoryID= request.GET.get('category')
    if categoryID:
        products = Product.get_all_products_by_Categoryid(categoryID)
    else:
        products = Product.get_all_products()  # get all products from product class


    data= {}   #Declare dictionary and pass values below
    data['products']= products
    data['categories']= categories
    return render(request, 'index.html',data)


def signup(request):
    return render(request, 'signup.html')