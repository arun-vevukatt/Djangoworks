from django.shortcuts import render

from django.http import HttpResponse, JsonResponse
from django.views import View

class Studentdetails(View):
    def get(self,request):
        data={'studentname':'amal','age':23,'course':'python','mark':78}
        return JsonResponse(data)

class StudentList(View):
    def get(self,request):
        data=[
            {'studentname': 'amal', 'age': 23, 'course': 'python', 'mark': 78},
            {'studentname': 'arun', 'age': 24, 'course': 'python', 'mark': 70},


        ]

        return JsonResponse(data,safe=False)

