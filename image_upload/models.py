from django.urls import reverse
from django.db import models


class Users_image(models.Model):
    name = models.TextField()
    imgfile = models.ImageField()
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('image-detail', args=[self.name])