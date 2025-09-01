from django.shortcuts import render
from django.http import HttpResponse


def index(request, id, name):
    return HttpResponse(f"Hello, {name} this is your id {id}")

def user(request, username):
    return HttpResponse(f"The username which is passed through it {username}")

def user_details(request,name,age,color):
    context ={
        'user_name' : name,
        'user_age' : age,
        'user_color' : color,
    }

    return render(request, 'variables.html', context)

def products(request):
    products_data = [
        {'id': 1, 'name': 'Wireless Mouse', 'price': 25, 'category': 'Electronics'},
        {'id': 2, 'name': 'Classic T-Shirt', 'price': 15, 'category': 'Apparel'},
        {'id': 3, 'name': 'Coffee Mug', 'price': 9, 'category': 'Kitchenware'},
        {'id': 4, 'name': 'Notebook & Pen Set', 'price': 19, 'category': 'Office Supplies'},
        {'id': 5, 'name': 'Bluetooth Speaker', 'price': 45, 'category': 'Electronics'},
    ]
    context = {
        'products': products_data,
    }
    return render(request, 'list_products.html', context)

