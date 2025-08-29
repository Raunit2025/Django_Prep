from django.shortcuts import render

# Create your views here.
def fruit_list(request):
    fruits = ["Apple","Mango","DragonFruit","Kiwi"]
    return render(request, 'fruits.html' ,{'fruits':fruits} )
def home(request):
    return render(request, 'home.html')

def monday_special(request):
    return render(request, 'monday.html')

def tuesday_special(request):
    return render(request, 'tuesday.html')