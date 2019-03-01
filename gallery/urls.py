from django.conf.urls import url, include
from django.contrib import admin
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url('^$', views.home, name='thehomepage'),
    url(r'^gallery/',views.gallery, name='thegallery'),
    url(r'^search/', views.search_results, name='search_results'),
]




