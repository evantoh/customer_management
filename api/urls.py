from . import views
from django.urls import path


app_name = 'api'
urlpatterns = [
    # customer Endpoints
    path('createCustomers/', views.CustomerListCreate.as_view(), name='customer-list-create'),

]