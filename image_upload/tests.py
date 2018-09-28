import os
from os.path import dirname
from os.path import join
from django.test import TestCase
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile
from .forms import UploadImageForm
from .models import Users_image


class UploadImageTests(TestCase):

    def setUp(self):
        super(UploadImageTests, self).setUp()
        base_dir = dirname(dirname(dirname(__file__)))
        self.image = join(base_dir, 'ij_test/media/blue.jpg')
        blue_image = Users_image(name='blue', imgfile=self.image)
        blue_image.save()

    def test_create(self):
        filename = (abs_dir_path, filename) = os.path.split(self.image)
        url = reverse('home')

        with open(self.image, 'rb') as infile:
            test_file = SimpleUploadedFile(filename, infile.read())
            data = {'imgfile': test_file, 'name': 'blue'}
            response = self.client.post(url, data, follow=True)

            self.assertEquals(response.status_code, 200)
            self.assertTemplateUsed('image/blue.html')

    def test_get_image(self):
        url = reverse('image-detail', kwargs={'name': 'blue'})
        data = {'name': 'blue'}
        images = Users_image.objects.filter(name='blue')
        
        response = self.client.post(url, data, follow=True)
        self.assertEquals(len(images), 1)
        self.assertEquals(response.status_code, 200) 

    def test_update(self):
        images = Users_image.objects.filter(name='blue')
        filename = (abs_dir_path, filename) = os.path.split(self.image)
        url = reverse('home')

        with open(self.image, 'rb') as infile:
            test_file = SimpleUploadedFile(filename, infile.read())
            data = {'imgfile': test_file, 'name': 'blue'}
            response = self.client.post(url, data, follow=True)

            self.assertEquals(response.status_code, 200)
            self.assertTemplateUsed('image/blue.html')
            self.assertEquals(len(images), 1)
