"""test_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from myapp import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.auth import views as auth_views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name='index'),
    url(r'^login/$',auth_views.login, name='login'),
    url(r'^redirect/',views.redirect, name='redirect'),
    url(r'^restaurant/$',views.restaurantindex),
    url(r'^reviews/$', views.reviews2),
    url(r'^restaurant/(?P<restauracja_id>[0-9]+)$',views.restaurantdetailed,name='detailed'),
    url(r'^restaurant/(?P<tag_name>[a-z]+)$',views.restaurantbytag,name='taged'),
    url(r'^backup/', views.backup),
    url(r'^recenzja/add/(?P<restauracja_id>[0-9a-z]*)$', views.RecenzjaStworz.as_view(), name='recenzja-add'),
    url(r'^restauracja/add/', views.RestauracjaStworz.as_view(), name='restauracja-add'),
    url(r'^register/', views.UserFormView.as_view(), name='register'),
    url(r'^team/', views.team, name='team'),
    url(r'^logout/$', auth_views.logout, {'next_page': 'redirect'}),
    url(r'^reviews/(?P<page>[0-9]+)$', views.reviews),
]

urlpatterns+= staticfiles_urlpatterns()