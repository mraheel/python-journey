from django.urls import path
from .views import SystemSettings, CountryList, StateListByCountry, CityListByState, LanguageList, TimezoneList

urlpatterns = [
    path('system/settings', SystemSettings.as_view(), name='system-settings'),

    path('data/countries/', CountryList.as_view(), name='country-list'),
    path('data/states/', StateListByCountry.as_view(), name='state-list-by-country'),
    path('data/cities/', CityListByState.as_view(), name='city-list-by-state'),
    
    path('data/languages/', LanguageList.as_view(), name='language-list'),
    path('data/timezones/', TimezoneList.as_view(), name='timezone-list'),
]
