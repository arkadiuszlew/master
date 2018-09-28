from django.db import models

class Users_image(models.Model):
    name = models.TextField()
    imgfile = models.ImageField()
    uploaded_at = models.DateTimeField(auto_now_add=True)