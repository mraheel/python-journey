from django.db import models

class SystemSetting(models.Model):
    key = models.CharField(max_length=30)
    value = models.CharField(max_length=255)

    class Meta:
        db_table = "settings"

    def __str__(self):
        return f'{self.key} - {self.value}'
        
class Country(models.Model):
    name = models.CharField(max_length=50, unique=True)
  
    class Meta:
        db_table = "countries"

    def __str__(self):
        return self.name

class State(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, unique=True)
  
    class Meta:
        db_table = "states"

    def __str__(self):
        return self.name

class City(models.Model):
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, unique=True)
  
    class Meta:
        db_table = "cities"

    def __str__(self):
        return self.name
    
class Language(models.Model):
    code = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=50, unique=True)
  
    class Meta:
        db_table = "languages"

    def __str__(self):
        return self.name

class Timezone(models.Model):
    name = models.CharField(max_length=50, unique=True)
  
    class Meta:
        db_table = "timezones"

    def __str__(self):
        return self.name
