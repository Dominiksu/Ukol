"""
URL configuration for _procejt project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myapp import views



urlpatterns = [

    path('', views.index_page),

    path('url-paths/', views.url_paths),
    
    path('calculator/', views.calculator),
    
    path('login/', views.login),
    
    path('test-template/', views.test_template),

    #path('jemno/jana/', views.my_page),
    #path('jemno/petr/', views.my_page),

    #path('jemno/karel/', views.my_page),

    path('jmeno/<str:name>/', views.my_page), #str:name parametr name musi byt na vstupu ve funkci ve views 

    path('clanky/<slug:name>-<int:number>/', views.article), 
    # clanky/jak-nasbirat-houby-1093283/ clanky/nejlepsi-mista-na-prochazku-762873
    # clanky/asaj_-14532-79790/

    
    #ukazat url cesty pomoí regex

    path('pages/<int:number>/<slug:name>', views.pages),
    
    path('age/', views.age),

    path('clock/', views.clock),
] 