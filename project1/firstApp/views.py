from django.shortcuts import render
from django.http import HttpResponse


def index(request, id, name):
    return HttpResponse(f"Hello, {name} this is your id {id}")

def user(request, username):
    return HttpResponse(f"The username which is passed through it {username}")
