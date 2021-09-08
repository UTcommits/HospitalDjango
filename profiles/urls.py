"""Hospital URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path, include
from . import views



urlpatterns = [
    path('', views.home,name ='home'),
    path('about/', views.about,name ='about'),
    path('contact/', views.contact,name ='contact'),
    
    path('register/', views.register, name="register"),
	path('login/', views.login_auth, name="login"),  
	path('logout/', views.logoutUser, name="logout"),


    path('profile/', views.patients_profile, name="profile"),
    path('profile/<str:pk>', views.create_profile, name="new_pat"),
    path('profile/del/<str:pk>', views.delPatient, name="del_pat"),
    path('crea_appoint/', views.create_appoint, name="crea_appoint"),
	path('invoice', views.patients_invoice, name="invoice"),  
	path('appointments', views.patient_appoint, name="appointments"),
    path('prescription', views.prescription, name="prescription"),
    path('prescription/new/<str:pk>', views.addpres, name='new_pres'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('err/', views.error, name='err'),
    

]
