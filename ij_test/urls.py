from django.contrib import admin
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path
from image_upload import views
from . import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.upload_file, name='home'),
    path('image/<name>/', views.image_view, name='image-detail'),
]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)