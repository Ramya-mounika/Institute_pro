"""instituepro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from instaapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.loginpage,name="loginpage"),
    path('login',views.loginpage,name='login'),
    path('logout',views.logoutpage,name="logout"),
    path('signup',views.signuppage,name="signup"),
    path('homepage',views.homepage,name="homepage"),
    path('contactpage',views.contactpage,name="contactpage"),
    path('servicespage',views.servicespage,name="servicespage"),
    path('feedbackpage',views.feedbackpage,name="feedbackpage"),
    path('delete/<id>',views.deletepage,name="delete"),
    path('gallerypage',views.gallerypage,name="gallerypage"),
    path('mainpage',views.mainpage,name="mainpage"),
    path('index',views.index)
]
