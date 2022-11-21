from django.urls import path
from . import views
app_name ='schooladmin'
urlpatterns=[
    path('home',views.schooladmin_home,name='sa_home'),
    path('addstudent',views.schooladmin_addstudent,name='sa_add'),
    path('viewstudent',views.schooladmin_viewstudent,name='sa_view'),
    path('attendance',views.schooladmin_viewattendance,name='sa_attendance'),
    path('example',views.schooladmin_master,name='sa_example')
]