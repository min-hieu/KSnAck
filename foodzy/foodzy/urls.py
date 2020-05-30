"""foodzy URL Configuration

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
from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from pages.views import home_view, queue_view
from users.views import (
    registerPage,
    loginPage,
    logoutPage,
    dynamicProfileLookup,
    Processing_page,
    )
from items.views import dynamicItemView

urlpatterns = [
    path('admin/', admin.site.urls, name='admin_page'),

    path('', home_view, name='home'),
    path('register/', registerPage, name='register'),
    path('login/', loginPage, name='login'),
    path('logout/', logoutPage, name='logout'),
    path('profiles/<slug:stuid>/', dynamicProfileLookup, name='profile'),
    path('queue/', queue_view, name='queue'),
    path('queue/accept/<slug:proid>', queue_view, name='queue_ac'),
    path('items/<slug:proid>/', dynamicItemView, name='item'),
    path('processing', Processing_page, name='processing'),
    path('processing/ac/<slug:proid>', Processing_page, name='pro_ac'),
]

urlpatterns += staticfiles_urlpatterns()
