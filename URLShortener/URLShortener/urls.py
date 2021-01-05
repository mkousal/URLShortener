"""URLShortener URL Configuration

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
from django.contrib.auth import views
from django.urls import path, include
from shortener.views import home_view, redirector, success_view, register, profile

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),
    path('success/<short_url>/', success_view, name='success-view'),
    path('accounts/', include('django.contrib.auth.urls')), 
    path('register/', register, name='register'),
    path('profile/', profile, name='profile'),
    path('<str:short_url>/', redirector),
]
