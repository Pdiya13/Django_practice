from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse("hello homepage!")
    return render(request,'website/index1.html')

def about(request):
    return HttpResponse("hello aboutpage!")

def contact(request):
    return HttpResponse("hello contactpage!")

def print(request):
    return render(request,'temp/hello.html')