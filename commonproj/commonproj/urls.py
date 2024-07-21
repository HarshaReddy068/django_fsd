"""
URL configuration for commonproj project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from app1.views import show_date                  # for Program-1
from app2.views import show_offset                # for Program-2
from app3.views import show_fruits_and_students   # for Program-3
from app4.views import homepage,aboutus,contactus # for Program-4
from app5.views import register,course_search     # for Program-5       No urls for Program-6
from app7.views import addProject                 # for Program-7
from app8.views import StudentListGenView, StudentDetailGenView # for Program-8
from app9.views import registerstudent, studentlist             # for Program-9
from app10.views import generate_csv_response, generate_pdf_response # for Program-10
from app11.views import course_search_with_ajax                   # for Program-11

urlpatterns = [
    path("admin/", admin.site.urls),
    path("prog1",show_date),                     # for Program-1
    re_path(r"^prog2/(\d{1,2})/$",show_offset),  # for Program-2
    path("prog3",show_fruits_and_students),      # for Program-3
    
    # for Program-4 
    path("home/",homepage),               
    path("aboutus/",aboutus),               
    path("contactus/",contactus),           
    
    # for program-5
    path("student",register),
    path("course",course_search),
    
    # for program-6 No views and Urls requried
    
    path("prog6",addProject), # for program-7
    
    # for program-8
    path("student_list/", StudentListGenView.as_view()),
    path('student_gen_detail/<int:pk>/', StudentDetailGenView.as_view()),
    
    # for program-9
    path('registerajax/', registerstudent, name='student_registration'),
    path('studentsajax/', studentlist, name='studentlist'),
    
    # for program-10
    path("generatecsv", generate_csv_response),
    path("generatepdf",generate_pdf_response),
    
    # for program-11
    path("course_search_ajax/", course_search_with_ajax),
        
]