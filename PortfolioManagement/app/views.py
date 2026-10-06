from django.shortcuts import render

from django.http import HttpResponse, JsonResponse
from django.views import View

class AboutAPI(View):
    def get(self,request):
        data={'id':101,'full name':'Arun Vevukatt','title':'Python Developer','email':'arunvevukatt007@gmail.com','contact':7356481224,'location':'Ernakulam','githuburl':'arun-vevukatt@github','linkedin url':'arun-vevukatt@linkedin'}
        return JsonResponse(data)

class EducationAPI(View):
    def get(self,request):
        data={'id':101,'institution':'Luminar','course':'python fullstack','university':'NACTET','location':'kakkanad','start year':2026,'end year':'2027','grade':'A+','Description':'good boy'}
        return JsonResponse(data)

class ProjectsAPI(View):
    def get(self,request):
        #data={'id':101,'project name':'python projects','descriptin':'basic python projects','technologies':'python,mysql,django','duration':'2 months','liveurl':'https://github.com/arun-vevukatt'}
        data = [
            {
                'id': 101,
                'project_name': 'Python Projects',
                'description': 'Basic Python projects',
                'technologies': 'Python, MySQL, Django',
                'duration': '2 months',
                'live_url': 'https://github.com/arun-vevukatt'
            },
            {
                'id': 101,
                'project_name': 'Hostel Management App',
                'description': 'Hostel management application',
                'technologies': 'Flutter, Firebase, Dart',
                'duration': '4 months',
                'live_url': 'https://github.com/arun-vevukatt'
            }
        ]
        return JsonResponse(data,safe=False)

class Home(View):
    def get(self,request):
        data="""
        ENDPOINTS
        /about
        /education
        /projects"""

        return HttpResponse(data)

