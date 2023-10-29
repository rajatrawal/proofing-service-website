"""
URL configuration for construction project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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

from django.urls import path
from . views import index,ServiceList,get_service,contact_form
urlpatterns = [
    path('', index,name='index'),
    path('service/<pk>',get_service),
    path('services/',ServiceList.as_view(),name='services'),
    path('contact/',contact_form,name='contact'),


]
