"""swati URL Configuration

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
from user import views
urlpatterns = [
    path('index',views.index,name='index'),
    path('newuser',views.newuser,name='newuser'),
    path('proregi',views.proregi,name='proregi'),
    path('indexi',views.indexi,name='indexi'),
    path('signin',views.signin,name='signin'),
    path('admin/', admin.site.urls),
    path('out',views.out,name='out'),
    path('edit',views.edit,name='edit'),
    path('update',views.update,name='update'),
    path('details',views.details,name='details'),
    path('',views.userindex,name=''),
    path('bstore',views.bstore,name='bstore'),
    

]
