from django.test import TestCase
from .models import Image
import datetime as dt

class ImageTestClass(TestCase):
    def setUp(self):
        '''create instance of image
        '''
        self.image1 = Image(image_name='faith', description='Mirror in the wall type of scenario', made_with= 'photoshop', location= 'california', category='Faith')

    def test_instance(self):
        self.assertTrue(isinstance(self.image1, Image))

    def save_image(self):
        '''saves image to database
        '''
        self.image1.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images) > 0)

    def delete_image(self):
        '''deletes image from database
        '''
        self.image.delete_image()
        images = Image.objects.all()
        self.assertTrue(len(images) == 0)
        

    def updte_image(self):
        '''saves image to database
        '''

    def get_image_by_id(self):
        '''saves image to database
        '''

    def search_image(self):
        '''saves image to database
        '''




    def tearDown(self):
        '''delete images in database
        '''


 
