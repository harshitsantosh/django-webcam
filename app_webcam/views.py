from django.shortcuts import render, redirect
import base64
from django.core.files.base import ContentFile
from .models import Camera
from django.contrib.auth.decorators import login_required
from .forms import RegistrationForm


@login_required()
def webcam(request):
    context = {
        'success': False
    }
    if request.method == 'POST':
        canvas_data = request.POST['canvasData']
        format, imgstr = canvas_data.split(';base64,')
        ext = format.split('/')[-1]
        pic = ContentFile(base64.b64decode(imgstr), name='temp.' + ext)
        camera = Camera.objects.create(file=pic)
        camera.save()
        context = {
            'success': True
        }

    return render(request, 'index.html', context)


def signup(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.save()
            return redirect('login')
    else:
        form = RegistrationForm()

    return render(request, 'signup.html', context={'form': form

                                                   })
