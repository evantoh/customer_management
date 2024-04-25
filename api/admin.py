from django.contrib import admin

from .models import Customer, Business, Location, CustomerBusinessLocation

# class BulkPostingFilesAdmin(admin.ModelAdmin):
#     list_display = ('name', 'status_date', 'status')
#     list_filter = ('name', 'status')
#     search_fields = ('status', )
#
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('customerName', 'phoneNumber', 'emailAddress')
    list_filter = ('customerName', 'phoneNumber')
    search_fields = ('customerName', 'phoneNumber')
class BusinessAdmin(admin.ModelAdmin):
    list_display = ('businessName', 'businessCategory', 'businessRegistrationDate', 'ageOfBusiness')
    list_filter = ('businessName', 'businessCategory')
    search_fields = ('businessName', 'businessCategory')

class LocationAdmin(admin.ModelAdmin):
    list_display = ('county', 'subCounty', 'ward', 'buildingName', 'floor')
    list_filter = ('county', 'subCounty')
    search_fields = ('county', 'subCounty')    
class CustomerBusinessLocationAdmin(admin.ModelAdmin):
    list_display = ('customer', 'business', 'location')
    list_filter = ('customer', 'business')
    search_fields = ('customer', 'business')        




admin.site.register(Customer, CustomerAdmin)
admin.site.register(Business, BusinessAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(CustomerBusinessLocation, CustomerBusinessLocationAdmin)

# Register your models here.
