from django.shortcuts import render
from django.http import HttpResponse


def index(request, id):
    return HttpResponse(f"Hello, world. You're at the firstApp index with index value: {id}")

def user(request, username):
    return HttpResponse(f"The username which is passed through it {username}")
