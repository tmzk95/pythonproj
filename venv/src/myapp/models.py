from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User
from django import forms
from django.core.urlresolvers import reverse
from django.shortcuts import render, render_to_response, redirect
from django.core.validators import MaxValueValidator, MinValueValidator

class Restauracja(models.Model):
    nazwa = models.CharField(max_length=200)
    zdjecie= models.CharField(max_length=300)
    opis = models.CharField(max_length=200)
    aktywna = models.BooleanField(default=False)

    @property
    def ocena(self):
        reviews = Recenzja.objects.filter(restauracja=self.id)
        rate = 0
        for review in reviews:
            rate += review.ocena
        if reviews.__len__() != 0:
            rate = rate / reviews.__len__()
        return "%.1f" %rate

    def __str__(self):
        return self.nazwa


class Recenzja(models.Model):
    opis= models.CharField(max_length=1500)
    ocena = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(10.0)])
    restauracja = models.ForeignKey(Restauracja, on_delete=models.CASCADE)
    uzytkownik = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.opis
    def get_absolute_url(self):
        return reverse('redirect')



