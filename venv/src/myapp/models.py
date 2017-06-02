from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User

class Restauracja(models.Model):
    nazwa = models.CharField(max_length=200)
    zdjecie= models.CharField(max_length=300)
    opis = models.CharField(max_length=200)
    ocena = models.FloatField()

    def __str__(self):
        return self.nazwa


class Recenzja(models.Model):
    opis= models.CharField(max_length=1500)
    ocena= models.FloatField()
    restauracja = models.ForeignKey(Restauracja, on_delete=models.CASCADE)
    uzytkownik = models.ForeignKey(User, on_delete=models.CASCADE)