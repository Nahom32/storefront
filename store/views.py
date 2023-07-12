from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import *
# Create your views here.
@api_view()
def product_list(request):
    return Response('ok')
@api_view()
def product_detail(request,id):
    return Response('the id returned is ' + str(id))

@api_view()
def customer_list(request,val):
    customer = Customer.objects.all()[:int(val)]
    lis = [CustomerSerializer(i).data for i in customer]
    
    return Response(lis)
@api_view()
def customer(request,id):
    customer = Customer.objects.get(pk=id)
    return Response(CustomerSerializer(customer).data)
    
    
