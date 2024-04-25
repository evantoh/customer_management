from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status


from rest_framework import generics
from .models import Customer, Business, Location, CustomerBusinessLocation
from rest_framework import permissions
from .serializers import CustomerSerializer, BusinessSerializer, LocationSerializer, CustomerBusinessLocationSerializer

# create and get customers
class CreateListCustomers(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    # permission_classes = [permissions.IsAuthenticated]


# retrieve, update and delete a specific customer
class CustomerRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Customer.objects.all()
    print("queryset", queryset)
    serializer_class = CustomerSerializer


    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        print("serializer_class", self.get_object())


        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)


