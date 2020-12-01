from django.db import models


class Camera(models.Model):
    file = models.FileField(upload_to='pic')
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
