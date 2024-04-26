from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework import viewsets
from rest_framework import permissions
from .models import Customer, Business, Location, CustomerBusinessLocation
from .serializers import CustomerSerializer, BusinessSerializer, LocationSerializer, CustomerBusinessLocationSerializer

# API view for creating and listing customers
class CreateListCustomers(generics.ListCreateAPIView):
    queryset = Customer.objects.all()  # Queryset for retrieving all customers
    serializer_class = CustomerSerializer  # Serializer class for serializing/deserializing customers



# API view for retrieving, updating, and deleting a specific customer
class CustomerRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]  # Permission class for accessing the view
    queryset = Customer.objects.all()  # Queryset for retrieving all customers
    serializer_class = CustomerSerializer  # Serializer class for serializing/deserializing customers

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()  # Get the customer instance to be deleted
        self.perform_destroy(instance)  # Perform the deletion
        return Response(status=status.HTTP_204_NO_CONTENT)  # Return success response




# Similar API views for Business and Location models...
class CreateListBusiness(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]  # Permission class for accessing the view
    queryset = Business.objects.all()
    serializer_class = BusinessSerializer



class BusinessRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]  # Permission class for accessing the view
    permission_classes = [permissions.IsAuthenticated]
    queryset = Business.objects.all()
    serializer_class = BusinessSerializer

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)



class CreateListLocation(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]  # Permission class for accessing the view
    queryset = Location.objects.all()
    serializer_class = LocationSerializer



class LocationRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)



# API view for retrieving, updating, and deleting a specific CustomerBusinessLocation instance
class CustomerBusinessLocationRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = CustomerBusinessLocation.objects.all()
    serializer_class = CustomerBusinessLocationSerializer

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)



# Viewset for CustomerBusinessLocation model
class CustomerBusinessLocationViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]  # Permission class for accessing the view
    queryset = CustomerBusinessLocation.objects.all()
    serializer_class = CustomerBusinessLocationSerializer
