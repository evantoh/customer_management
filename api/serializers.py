# Create serializers for each model to convert model instances to JSON representations and vice versa
from rest_framework import serializers
from .models import Customer, Business, Location, CustomerBusinessLocation

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

class CustomerBusinessLocationSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer()
    business = BusinessSerializer()
    location = LocationSerializer()

    class Meta:
        model = CustomerBusinessLocation
        fields = '__all__'