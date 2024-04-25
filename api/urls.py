from . import views
from django.urls import path


app_name = 'api'
urlpatterns = [
    # create/get customers dependent on the method 
    path('Customers/', views.CustomerListCreate.as_view(), name='customer-list-create'),


]