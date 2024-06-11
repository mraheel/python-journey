from django.urls import path
from .views import CountryList, StateListByCountry, CityListByState, LanguageList, TimezoneList

urlpatterns = [
    path('countries/', CountryList.as_view(), name='country-list'),
    path('states/', StateListByCountry.as_view(), name='state-list-by-country'),
    path('cities/', CityListByState.as_view(), name='city-list-by-state'),
    
    path('languages/', LanguageList.as_view(), name='language-list'),
    path('timezones/', TimezoneList.as_view(), name='timezone-list'),
]
