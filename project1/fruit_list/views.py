from django.shortcuts import render

# Create your views here.
def fruit_list(request):
    fruits = ["Apple","Mango","DragonFruit","Kiwi"]
    return render(request, 'fruit_list.html' ,{'fruits':fruits} )