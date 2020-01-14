"""gatinhos URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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

from gatinho.views import home, detail, delete, update
import dono.urls

urlpatterns = [
    path('', home),
    path('dono/', include('dono.urls')),
    path('detail/<int:id>', detail),
    path('delete/<int:id>', delete),
    path('update/<int:id>', update),
    path('admin/', admin.site.urls),
    path('account/', include('django.contrib.auth.urls'))
]
