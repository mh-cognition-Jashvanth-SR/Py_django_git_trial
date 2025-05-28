from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def say_hello(request):
    return HttpResponse("Hello Jashvanth! Welcome to your Django app.")
