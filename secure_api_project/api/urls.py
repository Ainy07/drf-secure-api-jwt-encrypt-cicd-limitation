from django.urls import path
from django.shortcuts import redirect
from .views import SecureDataListCreate

urlpatterns = [
    path('', lambda request: redirect('secure-data')),  
    path('secure-data/', SecureDataListCreate.as_view(), name='secure-data'),
]
