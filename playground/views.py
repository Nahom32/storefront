from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from store.models import Customer
from django.db.models import Q
#from store.models import Customer
# Create your views here.
def say_hello(request):
    query_set = list(Customer.objects.filter(Q(first_name__gt='C') & Q(last_name__gt='D')))
    
    return render(request, "hello.html",{'name': 'nahom','customers': query_set})
def say_bi(request):
    return HttpResponse("By")
