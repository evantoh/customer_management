from django.db import models

class Customer(models.Model):
    # Customer model representing information about customers
    customerName = models.CharField(max_length=100)  # Name of the customer
    phoneNumber = models.CharField(max_length=20, blank=True, null=True)  # Phone number of the customer
    emailAddress = models.EmailField(blank=True, null=True)  # Email address of the customer
    dateOfBirth = models.DateField(blank=True, null=True)  # Date of birth of the customer
    nationality = models.CharField(max_length=50, blank=True, null=True)  # Nationality of the customer

    def __str__(self):
        return self.customerName  # String representation of the customer model

class Business(models.Model):
    # Business model representing information about businesses
    businessName = models.CharField(max_length=100)  # Name of the business
    businessCategory = models.CharField(max_length=100, blank=True, null=True)  # Category of the business
    businessRegistrationDate = models.DateField(blank=True, null=True)  # Registration date of the business
    ageOfBusiness = models.IntegerField(blank=True, null=True)  # Age of the business

    def __str__(self):
        return self.businessName  # String representation of the business model
    
    def save(self, *args, **kwargs):
        if self.businessRegistrationDate:
            # Calculate the age of the business based on the current date
            today = date.today()
            registration_date = self.businessRegistrationDate
            self.ageOfBusiness = today.year - registration_date.year - ((today.month, today.day) < (registration_date.month, registration_date.day))
        super().save(*args, **kwargs)

class Location(models.Model):
    # Location model representing geographical location information
    county = models.CharField(max_length=50, blank=True, null=True)  # County of the location
    subCounty = models.CharField(max_length=50, blank=True, null=True)  # Sub-county of the location
    ward = models.CharField(max_length=50, blank=True, null=True)  # Ward of the location
    buildingName = models.CharField(max_length=100, blank=True, null=True)  # Name of the building
    floor = models.IntegerField(blank=True, null=True)  # Floor number of the building

    def __str__(self):
        return f"{self.buildingName}, {self.ward}, {self.subCounty}, {self.county}"  # String representation of the location model

class CustomerBusiness(models.Model):
    # CustomerBusiness model representing the relationship between customers and businesses
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)  # Reference to the customer
    business = models.ForeignKey(Business, on_delete=models.CASCADE)  # Reference to the business
    location = models.ForeignKey(Location, on_delete=models.CASCADE, blank=True, null=True)  # Optional reference to the location

    def __str__(self):
        return f"{self.customer.customerName} - {self.business.businessName} - {self.location}"  # String representation of the customer-business relationship
