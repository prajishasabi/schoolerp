from django.urls import path
from . import views
app_name='common'
urlpatterns=[
    path('',views.home,name='index'),
    path('adminlogin',views.adminlogin,name='admin_login'),
    path('teacherlogin',views.teacherlogin,name='teacher_login'),
    path('studentlogin',views.studentlogin,name='student_login')
]
