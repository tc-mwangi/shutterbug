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
    images=Image.
    return render(request, 'main/home.html', {"title":title})


def characters(request):
    '''renders characters page
    
    Arguments:
        request {[type]} -- [description]
    
    Returns:
        [type] -- [description]
    '''
    return render(request, 'main/characters.html')


def locations(request):
    '''renders characters page
    
    Arguments:
        request {[type]} -- [description]
    
    Returns:
        [type] -- [description]
    '''
    # try:
    #     image = Image.objects.get(id=location_id)
    # except DoesNotExist:
    #     raise Http404()

    return render(request, 'main/locations.html')


def search_results(request):

    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_images = Image.search_image_by_category(search_term)
        message = f"{search_term}"

        return render(request, 'main/search.html',{"message":message,"images": searched_images})

    else:
        message = "You haven't searched for any character"
        return render(request, 'main/search.html',{"message":message})


def modal(request):
    '''renders image modal
    
    Arguments:
        request {[type]} -- [description]
    
    Returns:
        [type] -- [description]
    '''
    return render(request, 'main/modal.html')