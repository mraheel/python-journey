from django.urls import path
from .views import CountryListCreate, CountryRetrieveUpdateDestroy

urlpatterns = [
    path('countries/', CountryListCreate.as_view(), name='country-list-create'),
    path('countries/<int:pk>/', CountryRetrieveUpdateDestroy.as_view(), name='country-detail'),
]
