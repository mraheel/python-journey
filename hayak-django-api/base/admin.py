from django.contrib import admin
from .models import Country, State, City, Language, Timezone

class CountryAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_filter = ['name']
    search_fields = ['name']

admin.site.register(Country, CountryAdmin)

class StateAdmin(admin.ModelAdmin):
    list_display = ['name', 'country']
    list_filter = ['name', 'country']
    search_fields = ['name', 'country__name']

admin.site.register(State, StateAdmin)

class CityAdmin(admin.ModelAdmin):
    list_display = ['name', 'state']
    list_filter = ['name', 'state']
    search_fields = ['name', 'state__name']

admin.site.register(City, CityAdmin)

class LanguageAdmin(admin.ModelAdmin):
    list_display = ['code', 'name']
    list_filter = ['code', 'name']
    search_fields = ['code', 'name']

admin.site.register(Language, LanguageAdmin)

class TimezoneAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_filter = ['name']
    search_fields = ['name']

admin.site.register(Timezone, TimezoneAdmin)