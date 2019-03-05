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

    class meta:
        ordering =['location_name']
    
    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()

    def update_location(self):
        self.update()


class Category(models.Model):
    '''creates instances of characters
    
    Arguments:
        models {[type]} -- [description]
    '''
    category_name = models.CharField(max_length=20)

    def __str__(self):
        return self.category_name

    class meta:
        ordering =['category_name']
    
    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()

    def update_category(self):
        self.update()


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
    article_image = models.ImageField(upload_to = 'articles/', null=True)
   

    def __str__(self):
        return self.image_name

    class meta:
        ordering = ['image_name']

  
    def save_image(self):
        '''save image to the database
        '''
        self.save()

    
    def delete_image(self):
        '''delete image from database
        '''
        self.delete()

    
    def update_image(self):
        '''update image in the database
        '''
        self.update()


    @classmethod
    def get_image_by_id(cls, id):
        '''retrieve images by id
        '''
        image=cls.objects.filter(id__id=id)
        return image

    @classmethod
    def search_image_by_category(cls, search_term):
        '''search image by category
        '''
        image = cls.objects.filter(upload_image__icontains=search_term)
        return image


    @classmethod
    def filter_by_location(cls, id):
        '''filter image by location
        '''
        image = cls.objects.filter(location__location= id)
        return image

    @classmethod
    def get_all(cls):
        "fetches all images"
        image = cls.objects.all()
        return image


         



    

