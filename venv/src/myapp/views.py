from django.shortcuts import render, render_to_response
from myapp import models
from django import http
from django import template


def index(request):
    return render_to_response('index.html')
def test(request):
    return render_to_response('login.html')

def register(request):
    if request.method == 'POST':
        uf = models.UserForm(request.POST, prefix='user')
        upf = models.UserProfileForm(request.POST, prefix='userprofile')
        if uf.is_valid() * upf.is_valid():
            user = uf.save()
            userprofile = upf.save(commit=False)
            userprofile.user = user
            userprofile.save()
            return http.HttpResponseRedirect('index.html')
    else:
        uf = models.UserForm(prefix='user')
        upf = models.UserProfileForm(prefix='userprofile')
    return render_to_response('registration.html',
                                               dict(userform=uf,
                                                    userprofileform=upf))