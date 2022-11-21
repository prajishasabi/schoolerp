from django.urls import path
from . import views
app_name='teacher'
urlpatterns=[
    path('home',views.teacher_home,name='tr_home'),
    path('viewstudent',views.teacher_studentview,name='tr_view'),
    path('profile',views.teacher_profile,name='tr_profile'),
    path('attendance',views.teacher_attendance,name='tr_attendance')
]