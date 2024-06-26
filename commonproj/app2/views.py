from datetime import timedelta
import datetime
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def show_offset(request,offset):
    offset=int(offset)
    now=datetime.datetime.now()
    ahead_time=now+timedelta(hours=offset)
    behind_time=now-timedelta(hours=offset)
    resp=f"<h2>Current date & time is %s</h2><h2>Date and time {offset} hrs ahead will be %s</h2><h2>Date and time {offset} hrs before will be %s</h2>"%(now,ahead_time,behind_time)
    return HttpResponse(resp)