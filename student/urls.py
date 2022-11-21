from django.urls import path
from . import views
app_name='student'
urlpatterns=[
    path('home',views.student_home,name='st_home'),
    path('changepswd',views.student_changepswd,name='st_chpswd'),
    path('profile',views.student_profile,name='st_profile'),
    path('attendance',views.student_attendance,name='attendance')
]