from django.urls import path, include
from .views import donation, charge

urlpatterns = [
    path('ask/', donation, name='ask'),
    path("donation/", charge, name="donation")
    
]