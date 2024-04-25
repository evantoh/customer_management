# Create serializers for each model to convert model instances to JSON representations and vice versa
from rest_framework import serializers
from .models import Customer, Business, Location, CustomerBusiness

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'

class BusinessSerializer(serializers.ModelSerializer):
    class Meta:
        model = Business
        fields = '__all__'

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'

class CustomerBusinessSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerBusiness
        fields = '__all__'
