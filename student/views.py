from django.shortcuts import render

# Create your views here.

def student_home(request):
    return render(request,'student/home.html')

def student_attendance(request):
    return render(request,'student/attendance.html')

def student_changepswd(request):
    return render(request,'student/changepswd.html')

def student_profile(request):
    return render(request,'student/profile.html')

    