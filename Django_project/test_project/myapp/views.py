from django.http import HttpResponse
from django.shortcuts import render
import random
import datetime as dt

# Create your views here.

# '' -> index page

def index_page(request):

    print(request.method)

    print(request.path)

    number = random.randint(1, 100)
    d = dt.datetime.now()

    return HttpResponse(f'''
                        <h1>Hello From Django: {number} | {d}</h1>
                        <img src="https://picsum.photos/200/300">
                        ''')

def url_paths(request):

    print(request.GET)

    print(request.GET['xyz'])

    print(request.GET.getlist('xyz'))

    return HttpResponse('This page is working')

def calculator(request):

    try:
        a = int(request.GET['a'])
        b = int(request.GET['b'])
        result = a + b
    except (KeyError, TypeError, ValueError):
        result = ''
    
    context = {
        'result' : result
    }
    return render(request, 'calculator.html', context)

def test_template(request):

    name = request.GET.get('name', 'World')
    age = request.GET.get('age', 0)

    context = {
        'date': dt.datetime.now(),
        'name': name,
        'age': age,
    }
    return render(request, 'test_template.html', context)

def clock(request):

    date = dt.datetime.now()
    return HttpResponse(f'''
                        <html>
                            <head>
                                <style>
                                    body{{
                                        background-color: lightpink;
                                        text-align: center;
                                    }}
                                </style>
                            </head>
                            <body>
                                <h1>{date.day:02}.{date.month:02}.{date.year}</h1>
                                <h2>{date.hour:02}:{date.minute:02}:{date.second:02}</h2>
                            </body>
                        </html>''')


def age(request):

    try:

        a = int(request.GET.get('a'))
        this_year = dt.datetime.now().year
        result = this_year - a
        message = f'Je vám přibližně {result} let'

    except (KeyError, TypeError, ValueError):

        result = 0
        message=''

    if result < 0:
        
        message = 'Nemožný věk'

    if result > 150:

        message = 'Nemožný věk'
    
    
    context = {
        'message': message,
        'age' : result,
    }
    return render(request, 'age.html', context)


