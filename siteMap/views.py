from django.shortcuts import render
from django.http import HttpResponseRedirect

# Create your views here.

def homeRedirect(request):
    return HttpResponseRedirect('/home')