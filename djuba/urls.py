from django.contrib import admin
from django.urls import path, include

urlpatterns = [
      path('', include('home.urls')),
      path('catalog', include('catalog.urls')),
]
