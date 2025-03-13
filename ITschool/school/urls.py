from django.urls import path
from school import views

app_name = 'school'

urlpatterns = [

    path('', views.index, name="index"),

    path('students/', views.students, name="students"),

    #path('course/', views.course, name= 'course'),
    
    #path('course/<int:pk>/', views.course_detail, name= 'course_detail'),

    path('course/', views.CourseList.as_view(), name= 'course'),

    path('course/<int:pk>/', views.CourseDetail.as_view(), name= 'course_detail'),
    
]
