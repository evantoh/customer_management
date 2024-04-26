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
    # URLs for handling customers
    path('customers/', views.CreateListCustomers.as_view(), name='createListCustomers'),  # Create and list customers
    path('customers/<int:pk>/', views.CustomerRetrieveUpdateDestroy.as_view(), name='customerRetrieveUpdateDelete'),  # Retrieve, update, or delete a specific customer

    # URLs for handling businesses
    path('businesses/', views.CreateListBusiness.as_view(), name='CreateListBusiness'),  # Create and list businesses
    path('businesses/<int:pk>/', views.BusinessRetrieveUpdateDestroy.as_view(), name='BusinessRetrieveUpdateDelete'),  # Retrieve, update, or delete a specific business

    # URLs for handling locations
    path('locations/', views.CreateListLocation.as_view(), name='CreateListLocation'),  # Create and list locations
    path('locations/<int:pk>/', views.LocationRetrieveUpdateDestroy.as_view(), name='LocationRetrieveUpdateDestroy'),  # Retrieve, update, or delete a specific location

    # URLs for handling customer-business-location associations
    path('customer-business-location/', views.CustomerBusinessLocationViewSet.as_view({
        'get': 'list',  # List all associations
        'post': 'create',  # Create a new association
        'put': 'update',  # Update an association
        'patch': 'partial_update',  # Partially update an association
        'delete': 'destroy'  # Delete an association
    })),
    path('customer-business-location/<int:pk>/', views.CustomerBusinessLocationViewSet.as_view({
        'get': 'retrieve',  # Retrieve a specific association
        'put': 'update',  # Update a specific association
        'patch': 'partial_update',  # Partially update a specific association
        'delete': 'destroy'  # Delete a specific association
    })),
]