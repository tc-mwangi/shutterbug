from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
import datetime as datetime
from .models import Image, Location, Category
# Create your views here.


def home(request):
    '''renders home page
    
    Arguments:
        request {[type]} -- [description]
    
    Returns:
        [type] -- [description]
    '''
    title = "shutterbug-showcase"
    return HttpResponse('This is Home', {"title":title})
    #return render(request, 'main/home.html')


def gallery(request):
    '''renders gallery page
    
    Arguments:
        request {[type]} -- [description]
    
    Returns:
        [type] -- [description]
    '''
    return HttpResponse('This is Gallery')
    #return render(request, 'main/gallery.html')


def search_results(request):
    '''renders search results
    
    Arguments:
        request {[type]} -- [description]
    
    Returns:
        [type] -- [description]
    '''
    return HttpResponse('This is Search')
    #return render(request, 'main/search.html')