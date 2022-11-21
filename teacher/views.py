from django.shortcuts import render

# Create your views here.

def teacher_home(request):
    return render(request,'teacher_templates/home.html')

def teacher_attendance(request):
    return render(request,'teacher_templates/attendance.html')

def teacher_studentview(request):
    return render(request,'teacher_templates/viewstudents.html')

def teacher_profile(request):
    return render(request,'teacher_templates/profile.html')

    