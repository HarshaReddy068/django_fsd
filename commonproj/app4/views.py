from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def homepage(request):
    return HttpResponse(render(request, "homepage.html"))

def aboutus(request):
    return HttpResponse(render(request, "aboutus.html"))

def contactus(request):
    return HttpResponse(render(request, "contactus.html"))


#add app4 to INSTALLED_APPS in commonproj/settings.py