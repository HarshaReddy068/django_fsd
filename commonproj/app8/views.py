from django.shortcuts import render
from django.views import generic

from app8.models import Student

# Create your views here.

class StudentListGenView(generic.ListView): 
    model=Student 
    template_name="student_gen_list.html" 
    
class StudentDetailGenView(generic.DetailView): 
    model=Student 
    template_name="student_gen_detail.html"
