from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'common/home.html')

def adminlogin(request):
    return render(request,'common/adminlogin.html')

def studentlogin(request):
    return render(request,'common/studentlogin.html')

def teacherlogin(request):
    return render(request,'common/teacherlogin.html')

