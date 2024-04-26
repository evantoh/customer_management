from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Customer,Business,Location,CustomerBusinessLocation
from datetime import datetime





class CustomerModelTest(TestCase):
    def test_create_customer(self):
        # Create a Customer instance
        customer = Customer.objects.create(
            customerName="Evans Test",
            phoneNumber="1234567890",
            emailAddress="test@evans.com",
            dateOfBirth="1997-01-01",
            nationality="Kenyan"
        )

        # Check if the instance was created successfully
        self.assertIsNotNone(customer)
        self.assertEqual(customer.customerName, "Evans Test")
        self.assertEqual(customer.phoneNumber, "1234567890")
        self.assertEqual(customer.emailAddress, "test@evans.com")
        self.assertEqual(customer.dateOfBirth, "1997-01-01")
        self.assertEqual(customer.nationality, "Kenyan")  

    def test_string_representation(self):
        # Create a Customer instance
        customer = Customer.objects.create(customerName="Evans Test")
        # Check if the string representation is as expected
        self.assertEqual(str(customer), "Evans Test")  
         
    def test_required_fields(self):
        # Attempt to create a Customer instance without required fields and check if an error is raised expected error "ValueError"
        with self.assertRaises(ValueError):
            Customer.objects.create()
    
class CustomerModelValidationTest(TestCase):
    def test_unique_email(self):
        # Create a Customer instance with a unique email address
        Customer.objects.create(customerName="Evans Test", emailAddress="evans@gmail.com")
        # Attempt to create another Customer with the same email address
        with self.assertRaises(ValueError):
            Customer.objects.create(customerName="Jane Kamau", emailAddress="evans@gmail.com")

    def test_unique_phone_number(self):
        # Create a Customer instance with a unique phone number
        Customer.objects.create(customerName="Evans Test", phoneNumber="1234567890")
        # Attempt to create another Customer with the same phone number
        with self.assertRaises(ValueError):
            Customer.objects.create(customerName="Jane Kamau", phoneNumber="1234567890")

    def test_maximum_length(self):
        # Attempt to create a Customer with fields exceeding maximum length
        with self.assertRaises(ValueError):
            Customer.objects.create(
                customerName="A" * 101,
                phoneNumber="1" * 21,
                nationality="N" * 51
            )

    def test_valid_date_of_birth(self):
        # Create a Customer instance with a valid date of birth
        Customer.objects.create(customerName="Evans Test", dateOfBirth="1990-01-01")
        # Verify that the instance was created successfully
        self.assertEqual(Customer.objects.count(), 1)

    def test_future_date_of_birth(self):
        # Attempt to create a Customer with a future date of birth
        with self.assertRaises(ValueError):
            Customer.objects.create(customerName="Evans Test", dateOfBirth="2050-01-01")
            

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