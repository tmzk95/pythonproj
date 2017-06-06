from django.shortcuts import render, render_to_response, redirect
from myapp import models
from django import http
from django import template
from django.contrib.auth import authenticate,login,logout
from django.views.generic import View
from .forms import UserForm
from django.http import HttpResponse
from .models import Restauracja,Recenzja,Tag,TagToRestaurant
from django.template import loader
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.shortcuts import get_object_or_404

def restaurantindex(request):
    all_restaurants= Restauracja.objects.filter(aktywna=True)
    all_tags=TagToRestaurant.objects.all()
    template= loader.get_template('restaurantindex.html')
    context= {
        'all_restaurants':all_restaurants,
        'all_tags':all_tags,

    }

    return HttpResponse(template.render(context,request))

def reviews(request):
    reviewsList = Recenzja.objects.filter().order_by('-id')[:5]
    template = loader.get_template('reviews.html')

    context = {
        'reviews': reviewsList
    }

    return HttpResponse(template.render(context, request))


def restaurantbytag(request,tag_name):
    tagstorestaurants= TagToRestaurant.objects.filter(tag=Tag.objects.get(name=tag_name))
    all_restaurants=[]
    all_tags = TagToRestaurant.objects.all()
    template = loader.get_template('restaurantindex.html')
    for tagtorestaurant in tagstorestaurants:
        all_restaurants.append(tagtorestaurant.restauracja)
    context= {
        'all_restaurants':all_restaurants,
        'all_tags':all_tags,
    }
    return HttpResponse(template.render(context, request))
def index(request):
    template= loader.get_template('index.html')
    if request.user.is_authenticated():
        context={
            'user':request.user.username,
        }
        return HttpResponse(template.render(context, request))
    else:
        return render_to_response('index.html')
def redirect(request):
    return render_to_response('redirect.html')
def team(request):
    return render_to_response('team.html')
def backup(request):
    return render_to_response('backup.html')
def test(request):
    return render_to_response('base.html')
def restaurantdetailed(request,restauracja_id):
    restaurant = Restauracja.objects.get(id=restauracja_id)
    reviews = Recenzja.objects.filter(restauracja_id=restauracja_id).order_by('-created')
    template = loader.get_template('restaurantdetail.html')
    context = {
        'restaurant': restaurant,
        'reviews' : reviews,
        'user':request.user.username,
    }

    return HttpResponse(template.render(context, request))

class RecenzjaStworz(CreateView):
    model = Recenzja
    fields = ['opis','ocena','restauracja']

    def get_initial(self):
        initials = super(RecenzjaStworz, self).get_initial()
        if self.kwargs['restauracja_id'] is not None:
            initials['restauracja'] = self.kwargs['restauracja_id']
        return initials

    def form_valid(self, form):
        user = self.request.user
        form.instance.uzytkownik = user
        return super(RecenzjaStworz, self).form_valid(form)


class UserFormView(View):
    form_class = UserForm
    template_name = 'registration.html'

    def get(self,request):
        form=self.form_class(None)
        return render(request,self.template_name, {'form':form})
    def post(self,request):
        form=self.form_class(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            user.set_password(password)
            user.save()

            user = authenticate(request,username=username,password=password)

            if user is not None:

                if user.is_active:
                    login(request, user)
                    return redirect('redirect.html')

        return render(request, 'index.html', {'form':form})


