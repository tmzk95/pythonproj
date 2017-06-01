from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User)

class UserForm(ModelForm):
    name = models.CharField(User)
    class Meta:
        model = User
        exclude = ['user']

class UserProfileForm(ModelForm):
    name = models.CharField(User)
    class Meta:
        model = UserProfile
        exclude = ['user']