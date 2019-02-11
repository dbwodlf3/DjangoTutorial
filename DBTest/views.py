from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def DBTest(request):
    return HttpResponse("hi")