from django.urls import path
from .views import SecureDataListCreate
def api_home(request):
    return JsonResponse({"message": "API root is working 🚀", "available_endpoints": ["/secure-data/", "/token/", "/token/refresh/"]})

urlpatterns = [
    path('', api_home),  
    path('secure-data/', SecureDataListCreate.as_view(), name="secure-data"),
]
