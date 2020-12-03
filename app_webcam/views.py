from django.shortcuts import render
import base64
from django.core.files.base import ContentFile
from .models import Camera


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
