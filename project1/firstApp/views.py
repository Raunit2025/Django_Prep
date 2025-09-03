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

def adding(request):
    
    value1 = request.GET.get('v1')
    if not value1:
        return HttpResponse("The value 1 is not here", status = 404)
    value2 = request.GET.get('v2')
    result = int(value1) + int(value2)
    return HttpResponse(f"The result of adding {value1} and {value2} is : {result}")

from django.http import HttpResponse

def calculate(request):
    try:
        v1 = float(request.GET.get('v1'))
        v2 = float(request.GET.get('v2'))
        op = request.GET.get('op')

        match op:
            case "add":
                return HttpResponse(v1 + v2)
            case "sub":
                return HttpResponse(v1 - v2)
            case "mul":
                return HttpResponse(v1 * v2)
            case "div":
                return HttpResponse(v1 / v2 if v2 != 0 else "Division by zero not allowed")
            case _:
                return HttpResponse("Invalid inputs")
    except Exception as e:
        return HttpResponse(f"Error: {e}")

        