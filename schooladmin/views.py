from django.shortcuts import render

# Create your views here.

def schooladmin_home(request):
    return render(request,'schooladmin/home.html')

def schooladmin_addstudent(request):
    return render(request,'schooladmin/addstudent.html')

def schooladmin_viewstudent(request):
    return render(request,'schooladmin/viewstudent.html')

def schooladmin_viewattendance(request):
    return render(request,'schooladmin/attendance.html')

def schooladmin_master(request):
    return render(request,'schooladmin/example.html')


    