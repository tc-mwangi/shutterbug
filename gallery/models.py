from django.db import models
import datetime as dt


class Location(models.Model):
    '''creates instances of locations
    
    Arguments:
        models {[type]} -- [description]
    '''
    location_name = models.CharField(max_length=20)

    def __str__(self):
        return self.location_name


class Category(models.Model):
    '''creates instances of category
    
    Arguments:
        models {[type]} -- [description]
    '''
    category_name = models.CharField(max_length=20)

    def __str__(self):
        return self.category_name


class Image(models.Model):
    '''creates instances of images
    
    Arguments:
        models {[type]} -- [description]
    '''
    image_name = models.CharField(max_length=20)
    description = models.TextField(max_length=50)
    made_with = models.CharField(max_length=20)
    location = models.ForeignKey(Location)
    category = models.ForeignKey(Category)
    post_date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.image_name

    class meta:
        ordering = ['img_name']

  
    def save_image(self):
        '''save image to the database
        '''
        self.save()

    
    def delete_image(self):
        '''delete image from database
        '''
        self.delete()

    @classmethod
    def update_image(self):
        '''update image in the database
        '''

    @classmethod
    def get_image_by_id(id):
        '''retrieve image by id
        '''

    @classmethod
    def search_image(cls, search_term):
        '''search image by category
        '''
        image = cls.objects.filter(category__icontains=search_term)
        return image


    @classmethod
    def filter_by_location(cls, search_term):
        '''filter image by location
        '''
        image = cls.objects.filter(location__icontains=search_term)
        return image



    

