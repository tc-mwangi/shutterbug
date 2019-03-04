from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
import datetime as datetime
from .models import Image, Location, Category


def home(request):
    '''renders home page
    
    Arguments:
        request {[type]} -- [description]
    
    Returns:
        [type] -- [description]
    '''
    title = "click-showcase"
    return render(request, 'main/home.html', {"title":title})


def characters(request):
    '''renders characters page
    
    Arguments:
        request {[type]} -- [description]
    
    Returns:
        [type] -- [description]
    '''
    return render(request, 'main/characters.html')


def search_results(request):
    '''renders search results
    
    Arguments:
        request {[type]} -- [description]
    
    Returns:
        [type] -- [description]
    '''
    return render(request, 'main/search.html')


def modal(request):
    '''renders image modal
    
    Arguments:
        request {[type]} -- [description]
    
    Returns:
        [type] -- [description]
    '''
    return render(request, 'main/modal.html')