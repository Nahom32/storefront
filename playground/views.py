from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def say_hello(request):
    return render(request, "hello.html",{'name': "Nahom"})
def say_bi(request):
    return HttpResponse("By")
