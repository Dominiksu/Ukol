from django.urls import path
from todo import views

'''
/todo/
todo/list/
todo/new/
todo/7627/'''

app_name = 'todo'

urlpatterns = [
    path('',views.index, name='index'),

    path('list/', views.todo_list, name='list'),

    path('new/', views.todo_new, name='new'),

    path('<int:number>/', views.todo_detail, name='detail'),

    path ('sign-up', views.sign_up, name= 'sign-up')
]