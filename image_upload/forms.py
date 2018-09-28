from django.forms import ModelForm
from file_uploader.models import Users_image


class UploadImageForm(ModelForm):
    class Meta:
        model = Users_image
        fields = ['name', 'imgfile']

