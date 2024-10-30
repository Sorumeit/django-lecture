from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render( request, "Firsrst_page/index.html", {
        "newyear": True
    } )