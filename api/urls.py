from . import views
from django.urls import path
from .views import *
from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
# router.register('data', GetMethod, basename='data')
urlpatterns = router.urls


app_name = 'api'
urlpatterns = [
    # create/get customers  
    path('customers/', views.CreateListCustomers.as_view(), name='createListCustomers'),
    # Retrieve a specific customer
    path('customers/<int:pk>/', views.CustomerRetrieveUpdateDestroy.as_view(), name='customerRetrieveUpdateDelete'),


    # create/get business 
    path('businesses/', views.CreateListBusiness.as_view(), name='CreateListBusiness'),
    # Retrieve a specific busisness
    path('businesses/<int:pk>/', views.BusinessRetrieveUpdateDestroy.as_view(), name='BusinessRetrieveUpdateDelete'),

    # create/get Location 
    path('locations/', views.CreateListLocation.as_view(), name='CreateListLocation'),
    # Retrieve a specific busisness
    path('locations/<int:pk>/', views.LocationRetrieveUpdateDestroy.as_view(), name='LocationRetrieveUpdateDestroy'),


    path('customer-business-location/', views.CustomerBusinessLocationListCreate.as_view(), name='CreateCustomerBusinessLocation'),
    path('customer-business-location/<int:pk>/', views.CustomerBusinessLocationRetrieveUpdateDestroy.as_view(), name='CustomerBusinessLocationRetrieveUpdateDestroy')

]