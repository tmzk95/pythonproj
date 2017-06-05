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
        return "%.1f" % rate

    @property
    def stars_orange(self):
        ocenaInt = int(float(self.ocena))
        stars = 'o'
        for star in range(1, ocenaInt):
            stars += 'o'
        for star in range(ocenaInt, 6):
            stars += 'e'
        return stars

    def __str__(self):
        return self.nazwa

    @property
    def tags(self):
        tagi=""
        tagslist= TagToRestaurant.objects.filter(restauracja=self.id)
        for tagtorestaurant in tagslist:
            tagi+=tagtorestaurant.tag.name
        return tagi






class Recenzja(models.Model):
    opis= models.CharField(max_length=1500)
    ocena = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(10.0)])
    restauracja = models.ForeignKey(Restauracja, on_delete=models.CASCADE)
    uzytkownik = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.opis
    def get_absolute_url(self):
        return '/restaurant/' + str(self.restauracja.id)

class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class TagToRestaurant(models.Model):
    restauracja=models.ForeignKey(Restauracja, on_delete=models.CASCADE)
    tag=models.ForeignKey(Tag, on_delete=models.CASCADE)

    @property
    def name(self):
        return self.tag.name
