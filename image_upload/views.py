from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from .forms import UploadImageForm
from .models import Users_image


def upload_file(request):
    if request.method == 'POST':
        image = _get_image(name=request.POST['name'])

        ##create
        if image is None:
            form = UploadImageForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()

        image = _get_image(name=request.POST['name'])
        return redirect(image)
    else:
        form = UploadImageForm()
    return render(request, 'users_image_form.html', {'form': form})

def _get_image(name):
    try:
        image = Users_image.objects.get(name=name)
    except:
        return None
    else:    
        return image

def image_view(request, name):
    image = get_object_or_404(Users_image, name=name)
    return render(request, 'users_image_detail.html', {'image': image, 'name': name}) 
