"""main URL Configuration

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
from django.urls import path
from webapp.views import book_index, book_create, book_update, book_delete, book_search


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', book_index, name='book_index'),
    path('create/', book_create, name='create'),
    path('update/<int:pk>/edit/', book_update, name='book_update'),
    path('delete/<int:pk>/delete/', book_delete, name='book_delete'),
    path('search/', book_search, name='book_search'),
]
