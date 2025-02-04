from django.shortcuts import render
import re

# Create your views here.


def index(request):
    return render(request, 'todo/index.html')

def todo_list(request):
    return render(request, 'todo/list.html')

def todo_new(request):
    return render(request, 'todo/new.html')

def todo_detail(request, number):
    return render(request, 'todo/detail.html')

def sign_up (request):
    
    password = request.POST.get('password', '')
    password_repeat =  request.POST.get('password_repeat', '')
   
    try: 
        if request.method == "POST" and password == password_repeat:
            return render(request, 'todo/signup_success.html')
        
        if request.method == "POST" and password != password_repeat:
            return render(request, 'todo/signup_failed.html')

    except (ValueError, KeyError, TypeError):
        raise (ValueError, KeyError, TypeError)




    
    context = {
        'password': password,
        'password_repeat': password_repeat,
        }

    return render(request, 'todo/signup.html', context)