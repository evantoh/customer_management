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

        # Retrieve or create Customer instance
        customer_instance = None
        if customer_data:
            customer_instance, _ = Customer.objects.get_or_create(**customer_data)

        # Retrieve or create Business instance
        business_instance = None
        if business_data:
            business_instance, _ = Business.objects.get_or_create(**business_data)

        # Retrieve or create Location instance if provided
        location_instance = None
        if location_data:
            location_instance, _ = Location.objects.get_or_create(**location_data)

        # Create CustomerBusinessLocation instance
        customer_business_location = CustomerBusinessLocation.objects.create(
            customer=customer_instance, business=business_instance, location=location_instance, **validated_data)

        return customer_business_location

    class Meta:
        model = CustomerBusinessLocation
        fields = '__all__'  # Serialize all fields of the CustomerBusinessLocation model
