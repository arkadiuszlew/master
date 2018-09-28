from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import messages
from django.shortcuts import get_object_or_404
from .forms import UploadImageForm
from .models import Users_image


def upload_file(request):
    if request.method == 'POST':
        name = request.POST['name']
        image = Users_image.objects.get(name=name)

        ##create
        if image is None:
            form = UploadImageForm(request.POST, request.FILES)
            if form.is_valid():
                messages.success(request, name + ' image uploaded')
                form.save()
        ##update
        if image:
            form = UploadImageForm(request.POST, request.FILES, instance=image)
            if form.is_valid():
                messages.success(request, name + ' image changed')
                form.save()
        form = UploadImageForm()
    else:
        form = UploadImageForm()
    return render(request, 'users_image_form.html', {'form': form})

def image_view(request, name):
    image = get_object_or_404(Users_image, name=name)
    return render(request, 'users_image_detail.html', {'image': image, 'name': name}) 
