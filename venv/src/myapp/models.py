from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User
from django import forms
from django.core.urlresolvers import reverse
from django.shortcuts import render, render_to_response, redirect

class Restauracja(models.Model):
    nazwa = models.CharField(max_length=200)
    zdjecie= models.CharField(max_length=300)
    opis = models.CharField(max_length=200)
    ocena = models.FloatField()
    aktywna = models.BooleanField(default=False)

    def __str__(self):
        return self.nazwa


class Recenzja(models.Model):
    opis= models.CharField(max_length=1500)
    ocena= models.FloatField()
    restauracja = models.ForeignKey(Restauracja, on_delete=models.CASCADE)
    uzytkownik = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.opis
    def get_absolute_url(self):
        return reverse('redirect')



