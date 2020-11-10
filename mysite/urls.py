"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index , name='views'),     #path(' homepage dikhega ' , file ka name.function ka name , name=' ek naam dedo kuch bhi ')
    path('about', views.about, name='about'),   

    path('nevigator' , views.nevigator , name='nevigator'),
    
    
    path('analyze/' , views.analyze , name= 'analyze'),
    path('analyzer/' , views.analyzer , name= 'analyzer'),
]
