from django.shortcuts import render, render_to_response, redirect
from myapp import models
from django import http
from django import template
from django.contrib.auth import authenticate,login
from django.views.generic import View
from .forms import UserForm
from django.http import HttpResponse
from .models import Restauracja,Recenzja
from django.template import loader

def restaurantindex(request):
    all_restaurants= Restauracja.objects.all()
    template= loader.get_template('restaurantindex.html')
    context= {
        'all_restaurants':all_restaurants,
    }

    return HttpResponse(template.render(context,request))

def index(request):
    return render_to_response('index.html')
def backup(request):
    return render_to_response('backup.html')
def test(request):
    return render_to_response('login.html')
def restaurantdetailed(request,restauracja_id):
    restaurant = Restauracja.objects.get(id=restauracja_id)
    reviews = Recenzja.objects.filter(restauracja_id=restauracja_id)
    template = loader.get_template('restaurantdetail.html')
    context = {
        'restaurant': restaurant,
        'reviews' : reviews,
    }

    return HttpResponse(template.render(context, request))
