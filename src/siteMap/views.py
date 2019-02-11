from django.shortcuts import render
from django.http import HttpResponseRedirect

# Create your views here.

def homeRedirect(request):
    return HttpResponseRedirect('/home')

def home(request):
    return render(request, 'siteMap/layout.html')