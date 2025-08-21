from django.urls import path
from django.shortcuts import redirect
from . import views

urlpatterns = [
    path('', lambda request: redirect('secure-data')),  # 👈 redirect karega
    path('secure-data/', views.secure_data, name='secure-data'),
]
