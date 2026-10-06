from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def Home(request):
    print(request.method)
    if(request.method=="GET"):
        return HttpResponse("WELCOME TO DJANGO")

def Index(request):
    print(request.method)
    if (request.method == "GET"):
        return HttpResponse("INDEX")

