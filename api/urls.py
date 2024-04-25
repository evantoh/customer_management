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
    # create/get customers dependent on the method 
    path('customers/', views.CreateListCustomers.as_view(), name='createListCustomers'),

    # Retrieve a specific customer
    path('customers/<int:pk>/', views.CustomerRetrieveUpdateDestroy.as_view(), name='customerRetrieveUpdateDelete'),





]