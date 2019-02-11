from django.shortcuts import render
from django.http import HttpResponse
import json

from .forms import NameForm

# Create your views here.
def FormTest(request):
    if request.method == 'POST':   
        form = NameForm(request.POST)
        if form.is_valid():
            return HttpResponse(form.cleaned_data['your_name'])
    else:
        form = NameForm()
    return render(request, 'FormTest/index.html', {'form': form})