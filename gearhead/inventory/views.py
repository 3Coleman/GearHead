from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def inventory_view(request):
    return HttpResponse("Helo world")
