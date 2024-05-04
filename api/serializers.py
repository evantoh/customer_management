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

    def create(self, validated_data):
        # Extract nested serializer data
        customer_data = validated_data.pop('customer', None)
        business_data = validated_data.pop('business', None)
        location_data = validated_data.pop('location', None)

        # Create or retrieve Customer instance
        # Check if customer_data is provided
        business_instance = None
        if customer_data:
            # If customer_data is provided, attempt to retrieve an existing Customer instance
            # or create a new one if it doesn't exist
            customer_instance, _ = Customer.objects.get_or_create(**customer_data)

        # Create or retrieve Business instance
        if business_data:
            # If business_data is provided, attempt to retrieve an existing Business instance
            # or create a new one if it doesn't exist
            business_instance, _ = Business.objects.get_or_create(**business_data)

        # Create CustomerBusinessLocation instance
        customer_business_location = CustomerBusinessLocation.objects.create(
            customer=customer_instance, business=business_instance, **validated_data)

        # Create or update related models
        if location_data:
            # If location_data is provided, attempt to retrieve an existing Location instance
            # or create a new one if it doesn't exist
            location_instance, _ = Location.objects.get_or_create(**location_data)
            customer_business_location.location = location_instance

        customer_business_location.save()

        return customer_business_location

    class Meta:
        model = CustomerBusinessLocation
        fields = '__all__'  # Serialize all fields of the CustomerBusinessLocation model