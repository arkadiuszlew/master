from django.forms import ModelForm
from image_upload.models import Users_image


class UploadImageForm(ModelForm):
    class Meta:
        model = Users_image
        fields = ['name', 'imgfile']

