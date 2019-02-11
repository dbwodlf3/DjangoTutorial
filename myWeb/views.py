from django.http import HttpResponse
from django.shortcuts import render

import datetime

def current_datetime(request):
    now = datetime.datetime.now()
    html = "It is now %s." % now
    return HttpResponse(html)

def test_template(request, user_id):
    return render(request, "myWeb/index.html", {"user_id": user_id})