from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Customer,Business,Location,CustomerBusinessLocation

class CustomerBusinessLocationAPITest(TestCase):
    def setUp(self):
        # Create test data for Customer, Business, and Location models
        self.customer = Customer.objects.create(customerName="Test Customer")
        self.business = Business.objects.create(businessName="Test Business")
        self.location = Location.objects.create(buildingName="Test Building")

    def test_create_customer_business_location(self):
        # Create a CustomerBusinessLocation instance
        cbl = CustomerBusinessLocation.objects.create(
            customer=self.customer,
            business=self.business,
            location=self.location
        )
        # Check if the instance was created successfully
        self.assertIsNotNone(cbl)
        self.assertEqual(cbl.customer, self.customer)
        self.assertEqual(cbl.business, self.business)
        self.assertEqual(cbl.location, self.location)

    def test_string_representation(self):
        # Create a CustomerBusinessLocation instance
        cbl = CustomerBusinessLocation.objects.create(
            customer=self.customer,
            business=self.business,
            location=self.location
        )
        # Check if the string representation is as expected
        expected_string = f"{self.customer.customerName} - {self.business.businessName} - {self.location}"
        self.assertEqual(str(cbl), expected_string)