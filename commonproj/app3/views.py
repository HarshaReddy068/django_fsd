from django.template import loader
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def show_fruits_and_students(request):
    template=loader.get_template("mytemplate.html")
    
    ctx={
        "fruits":["Apple","Banana","Mango"],
        "selected_students":["Ajay","Karthik","Preethi","Ramesh","Ramya"]
    }
    return HttpResponse(template.render(ctx,request))



# add app3 in INSTALLED_APPS in settings.py