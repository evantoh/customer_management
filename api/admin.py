from django.contrib import admin
from .models import Customer, Business, Location, CustomerBusinessLocation

class CustomerAdmin(admin.ModelAdmin):
    """
    Admin configuration for the Customer model.
    """
    list_display = ('customerName', 'phoneNumber', 'emailAddress')  # Display these fields in the list view
    list_filter = ('customerName', 'phoneNumber')  # Add filters based on these fields
    search_fields = ('customerName', 'phoneNumber')  # Enable searching based on these fields

class BusinessAdmin(admin.ModelAdmin):
    """
    Admin configuration for the Business model.
    """
    list_display = ('businessName', 'businessCategory', 'businessRegistrationDate', 'ageOfBusiness')  # Display these fields in the list view
    list_filter = ('businessName', 'businessCategory')  # Add filters based on these fields
    search_fields = ('businessName', 'businessCategory')  # Enable searching based on these fields

class LocationAdmin(admin.ModelAdmin):
    """
    Admin configuration for the Location model.
    """
    list_display = ('county', 'subCounty', 'ward', 'buildingName', 'floor')  # Display these fields in the list view
    list_filter = ('county', 'subCounty')  # Add filters based on these fields
    search_fields = ('county', 'subCounty')  # Enable searching based on these fields

class CustomerBusinessLocationAdmin(admin.ModelAdmin):
    """
    Admin configuration for the CustomerBusinessLocation model.
    """
    list_display = ('customer_name', 'business_name', 'location')  # Display these fields in the list view
    list_filter = ('customer__customerName', 'business__businessName')  # Add filters based on related fields
    search_fields = ('customer__customerName', 'business__businessName')  # Enable searching based on related fields

    def customer_name(self, obj):
        """
        Display the customer name for CustomerBusinessLocation objects.
        """
        return obj.customer.customerName

    def business_name(self, obj):
        """
        Display the business name for CustomerBusinessLocation objects.
        """
        return obj.business.businessName

# Register the admin configurations for each model
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Business, BusinessAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(CustomerBusinessLocation, CustomerBusinessLocationAdmin)


