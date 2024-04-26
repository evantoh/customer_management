from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Customer,Business,Location,CustomerBusinessLocation
from datetime import datetime
from datetime import date



# Unit Testing on the Customer Model
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
    # Validation Tests on the Customer Model 
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

    # Boundary Tests on the Customer Model
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



class BusinessModelTestCase(TestCase):
    def setUp(self):
        # Create a sample business for testing
        self.business = Business.objects.create(
            businessName='Test Business',
            businessCategory='Test Category',
            businessRegistrationDate=date(2020, 1, 1)
        )

    def test_age_of_business_calculation(self):
        #Test that the age of the business is calculated correctly.
        
        # Calculate expected age of the business
        today = date.today()
        registration_date = self.business.businessRegistrationDate
        expected_age = today.year - registration_date.year - ((today.month, today.day) < (registration_date.month, registration_date.day))

        # Retrieve the saved business object from the database
        saved_business = Business.objects.get(businessName='Test Business')

        # Check if the calculated age matches the expected age
        self.assertEqual(saved_business.ageOfBusiness, expected_age) 

    def test_str_method(self):
        # Test the __str__ method of the Business model.

        self.assertEqual(str(self.business), 'Test Business')

    def test_optional_fields(self):
        # Test that optional fields can be left blank or null.
        # Create a business without specifying optional fields
        business_without_optional_fields = Business.objects.create(
            businessName='Another Test Business'
        )

        # Retrieve the saved business object from the database
        saved_business = Business.objects.get(businessName='Another Test Business')

        # Check that optional fields are None
        self.assertIsNone(saved_business.businessCategory)
        self.assertIsNone(saved_business.businessRegistrationDate)
        self.assertIsNone(saved_business.ageOfBusiness)

    def test_save_method(self):
        # Test that the save method correctly calculates the age of the business.
 
        # Create a new business with a registration date
        new_business = Business.objects.create(
            businessName='New Business',
            businessRegistrationDate=date(2019, 1, 1)
        )

        # Retrieve the saved business object from the database
        saved_business = Business.objects.get(businessName='New Business')

        # Calculate expected age of the business
        today = date.today()
        registration_date = saved_business.businessRegistrationDate
        expected_age = today.year - registration_date.year - ((today.month, today.day) < (registration_date.month, registration_date.day))

        # Check if the calculated age matches the expected age
        self.assertEqual(saved_business.ageOfBusiness, expected_age) 

class LocationModelTestCase(TestCase):
    def setUp(self):
        # Create a sample location for testing
        self.location = Location.objects.create(
            county='Test County',
            subCounty='Test Sub-County',
            ward='Test Ward',
            buildingName='Test Building',
            floor='1'
        )

    def test_str_method(self):
        # Test the __str__ method of the Location model.
        self.assertEqual(str(self.location), 'Test Building, Test Ward, Test Sub-County, Test County')

    def test_optional_fields(self):
        # Test that optional fields can be left blank or null.
   
        # Create a location without specifying optional fields
        location_without_optional_fields = Location.objects.create(
            county='Another County',
            subCounty='Another Sub-County',
            ward='Another Ward'
        )

        # Retrieve the saved location object from the database
        saved_location = Location.objects.get(county='Another County')

        # Check that optional fields are None
        self.assertIsNone(saved_location.buildingName)
        self.assertIsNone(saved_location.floor)

    def test_blank_fields(self):
        # Test that fields with blank=True allow empty string values.
 
        # Create a location with blank values for optional fields
        location_with_blank_fields = Location.objects.create(
            county='Blank County',
            subCounty='Blank Sub-County',
            ward='Blank Ward',
            buildingName='',
            floor=''
        )

        # Retrieve the saved location object from the database
        saved_location = Location.objects.get(county='Blank County')

        # Check that optional fields are saved as empty strings
        self.assertEqual(saved_location.buildingName, '')
        self.assertEqual(saved_location.floor, '')

    def test_null_fields(self):
        # Test that fields with null=True allow null values.

        # Create a location with null values for optional fields
        location_with_null_fields = Location.objects.create(
            county='Null County',
            subCounty='Null Sub-County',
            ward='Null Ward',
            buildingName=None,
            floor=None
        )

        # Retrieve the saved location object from the database
        saved_location = Location.objects.get(county='Null County')

        # Check that optional fields are saved as None
        self.assertIsNone(saved_location.buildingName)
        self.assertIsNone(saved_location.floor)                 