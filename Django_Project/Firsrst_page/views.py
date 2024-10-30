from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

def index(request):
    time = datetime.now();
    return render( request, "Firsrst_page/index.html", {
        "newyear": time.day == 1 and time.month == 1
    } )