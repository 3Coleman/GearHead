

from django.contrib import admin
from django.urls import path, include
from . views import inventory_view

urlpatterns = [
    path('', inventory_view)
]
