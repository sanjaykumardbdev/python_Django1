from django.shortcuts import render
from django.urls import path
from django.http import HttpResponse


# Create your views here.


def home(request):
    # return HttpResponse("<h1>Hello World</h1>")
    return render(request, 'home.html')


def add(request):
    val1 = int(request.POST['num1'])
    val2 = int(request.POST['num2'])
    res = val1 + val2
    return render(request, "result.html", {'result': res})

def add_name(request):
    val1 = request.POST['fname']
    val2 = request.POST['lname']
    res = val1 + ' ' + val2
    return render(request, "result.html", {'fullname': res})
