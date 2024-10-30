from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

def index(request):
    return render( request, "Firsrst_page/index.html", {
        "newyear": datetime.now.day == 1 and datetime.now.month == 1
    } )