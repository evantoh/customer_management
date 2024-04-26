from rest_framework import serializers
from .models import Customer, Business, Location, CustomerBusinessLocation

class CustomerSerializer(serializers.ModelSerializer):
    """
    Serializer for the Customer model.
    """
    class Meta:
        model = Customer
        fields = '__all__'  # Serialize all fields of the Customer model

class BusinessSerializer(serializers.ModelSerializer):
    """
    Serializer for the Business model.
    """
    class Meta:
        model = Business
        fields = '__all__'  # Serialize all fields of the Business model

class LocationSerializer(serializers.ModelSerializer):
    """
    Serializer for the Location model.
    """
    class Meta:
        model = Location
        fields = '__all__'  # Serialize all fields of the Location model

class CustomerBusinessLocationSerializer(serializers.ModelSerializer):
    """
    Serializer for the CustomerBusinessLocation model.
    """
    # Include serializers for related models to provide nested representations
    customer = CustomerSerializer()  # Serialize related Customer model
    business = BusinessSerializer()  # Serialize related Business model
    location = LocationSerializer()  # Serialize related Location model

    class Meta:
        model = CustomerBusinessLocation
        fields = '__all__'  # Serialize all fields of the CustomerBusinessLocation model
