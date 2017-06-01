from django.shortcuts import render, render_to_response, redirect
from myapp import models
from django import http
from django import template
from django.contrib.auth import authenticate,login
from django.views.generic import View
from .forms import UserForm

def index(request):
    return render_to_response('index.html')
def test(request):
    return render_to_response('login.html')

class UserFormView(View):
    form_class=UserForm
    template_name='registration.html'

    def get(self,request):
        form=self.form_class(None)
        return render(request, self.template_name, {'form':form})
    def post(self,request):
        form=self.form_class(request.POST)

        if form.is_valid():
            user=form.save(commit=False)
            username = form.cleaned_data('username')
            password = form.cleaned_data('password')
            user.user=request.user
            user.save()
            user=authenticate(username=username,password=password)

            if user.is_active:
                login(request,user)
                return redirect('index')

        return render(request, self.template_name, {'form': form})

