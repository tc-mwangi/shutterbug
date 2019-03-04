from django.conf.urls import url, include
from django.contrib import admin
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url('^$', views.home, name='homepage'),
    url(r'^characters/',views.characters, name='characters'),
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^modal/', views.modal, name='modal'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)


