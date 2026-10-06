# from django.shortcuts import render
# from django.http import HttpResponse
#
# def FirstPage(request):
#     print(request.method)
#     if(request.method=="GET"):
#         return HttpResponse("FIRST PAGE")
#
# def SecondPage(request):
#     print(request.method)
#     if (request.method == "GET"):
#         return HttpResponse("SECOND PAGE")


from django.http import HttpResponse
from django.views import View

class First(View):
    def get(self,request):
        return HttpResponse("First Page")

class Second(View):
    def get(self,request):
        return HttpResponse("Second page")