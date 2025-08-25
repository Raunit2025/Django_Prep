from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return ("This is the index view")
def add_todo(request):
    return ("This is the ToDo Add view")
def complete_todo(request, id):
    return ("The task with id : {id} is completed")
def delete_todo(request, id):
    return ("The task with id : {id} is deleted")