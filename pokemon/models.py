from django.contrib.auth.models import User
from django.db import models



class Pokemon(models.Model):
    name = models.CharField(max_length=100, null=False)
    description = models.TextField(null=True)
    type = models.CharField(max_length=32, null=True)
    picture = models.URLField(null=True)
    video = models.CharField(max_length=64, null=True)
    url = models.URLField(null=True)
    favicon = models.URLField(null=True)


    def __str__(self):
        return self.name




class Favorite(models.Model):
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE)
    user_id = models.IntegerField()
