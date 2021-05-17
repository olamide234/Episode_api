from django.db import models

# Create your models here.
class Location(models.Model):
    name = models.CharField(max_length=64)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    created = models.DateTimeField(auto_now_add=True)

class Comments(models.Model):
    comments = models.TextField(max_length=249)
    ipAddressLocation = models.GenericIPAddressField()
    created = models.DateTimeField(auto_now_add=True)

class Episode(models.Model):
    name = models.CharField(max_length=64)
    released_date = models.DateTimeField(auto_now_add=True)
    episodeCode = models.CharField(max_length=64)
    characters = models.ManyToManyField('Character') #Use quoted model name for model class called when it hasn't been defined 
    episodeComments = models.ManyToManyField(Comments)
    created = models.DateTimeField(auto_now_add=True)

class Character(models.Model):
    AC = 'AC'
    DD = 'DD'
    UK = 'UK'
    M = 'M'
    F = 'F'
    
    STATUS_CODE=[
        (AC, 'Active'),
        (DD, 'Dead'),
        (UK, 'Unknown')
    ]

    SEX = [
        (M, 'Male'),
        (F, 'Female')
    ]

    firstName = models.CharField(max_length=64)
    lastName = models.CharField(max_length=64)
    status = models.CharField(choices=STATUS_CODE, max_length=2)
    stateOfOrigin = models.CharField(max_length=64, blank=True)
    gender = models.CharField(choices=SEX, max_length=1)
    location = models.OneToOneField(Location, on_delete=models.CASCADE, blank=True, null=True)
    episodes = models.ForeignKey(Episode, on_delete=models.CASCADE, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)



