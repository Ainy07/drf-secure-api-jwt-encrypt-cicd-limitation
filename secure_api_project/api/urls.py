from django.urls import path
from .views import SecureDataListCreate

urlpatterns = [
    path('secure-data/', SecureDataListCreate.as_view(), name="secure-data"),
]
