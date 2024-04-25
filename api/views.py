from django.shortcuts import render
from rest_framework import generics
from .models import Customer, Business, Location, CustomerBusiness
from .serializers import CustomerSerializer, BusinessSerializer, LocationSerializer, CustomerBusinessSerializer

# Create your views here.

class CustomerListCreate(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
