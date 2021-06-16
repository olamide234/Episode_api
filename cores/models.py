from django.db import models

# Create your models here.
class Location(models.Model):
    name = models.CharField(max_length=128)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    character_id = models.OneToOneField('Character', on_delete=models.CASCADE, related_name='location', blank=True, null=True)#
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Comment(models.Model):
    comments = models.TextField(max_length=249)
    ipAddressLocation = models.GenericIPAddressField()
    created = models.DateTimeField(auto_now_add=True)
    episode = models.ForeignKey('Episode', related_name='episodeComments', on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.comments


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
    episodes = models.ManyToManyField('Episode', blank=True)#Use quoted model name for model class called when it hasn't been defined
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.firstName +  ' ' + self.lastName

class Episode(models.Model):
    name = models.CharField(max_length=64)
    released_date = models.DateTimeField(auto_now_add=True)
    episodeCode = models.CharField(max_length=64)
    characters = models.ManyToManyField(Character)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    # this function can be use for serializer "get_count_comments()"
    # def count_comments(self):
    #     return self.episodeComments.all().count()
