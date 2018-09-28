from django.contrib import admin
from django.urls import path
from image_upload import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.upload_file, name='home'),
]
