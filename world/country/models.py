from django.db import models

# Create your models here.

class Country(models.Model):
    code = models.CharField(primary_key=True, max_length=3)  # Field name made lowercase.
    name = models.CharField(max_length=52)  # Field name made lowercase.
    continent = models.CharField(max_length=13)  # Field name made lowercase.
    region = models.CharField(max_length=26)  # Field name made lowercase.
    surfacearea = models.DecimalField(max_digits=10, decimal_places=2)  # Field name made lowercase.
    indepyear = models.SmallIntegerField(blank=True, null=True, default='')  # Field name made lowercase.
    population = models.IntegerField()  # Field name made lowercase.
    lifeexpectancy = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True, default='')  # Field name made lowercase.
    gnp = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, default='')  # Field name made lowercase.
    gnpold = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, default='')  # Field name made lowercase.
    localname = models.CharField(max_length=45)  # Field name made lowercase.
    governmentform = models.CharField(max_length=45)  # Field name made lowercase.
    headofstate = models.CharField(max_length=60, blank=True, null=True,default='')  # Field name made lowercase.
    capital = models.IntegerField(blank=True, null=True, default='')  # Field name made lowercase.
    code2 = models.CharField(max_length=2)  # Field name made lowercase.

    def __str(self):
        return self.code

class City(models.Model):
    name = models.CharField(max_length=35)  # Field name made lowercase.
    countrycode = models.ForeignKey(Country, on_delete=models.CASCADE)  # Field name made lowercase.
    district = models.CharField(max_length=20)  # Field name made lowercase.
    population = models.IntegerField()  # Field name made lowercase.


class Countrylanguage(models.Model):
    countrycode = models.OneToOneField(Country, on_delete=models.CASCADE, primary_key=True)  # Field name made lowercase.
    language = models.CharField(max_length=30)  # Field name made lowercase.
    isofficial = models.CharField(max_length=1)  # Field name made lowercase.
    percentage = models.DecimalField(max_digits=4, decimal_places=1)  # Field name made lowercase.