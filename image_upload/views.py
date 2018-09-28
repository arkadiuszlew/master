from django.shortcuts import render

def upload_file(request):
    return render(request, 'users_image_form.html', {})
