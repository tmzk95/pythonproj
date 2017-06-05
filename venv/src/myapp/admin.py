from django.contrib import admin
from .models import Recenzja,Restauracja,Tag,TagToRestaurant

# Register your models here.
admin.site.register(Restauracja)
admin.site.register(Recenzja)
admin.site.register(Tag)
admin.site.register(TagToRestaurant)