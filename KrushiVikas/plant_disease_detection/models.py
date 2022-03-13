import os

from django.db import models


def upload_path(instance, filename):
    return os.path.join("uploads", filename)


class ImageModel(models.Model):
    image = models.ImageField(upload_to=upload_path, null=False, blank=True)
    created_date = models.DateTimeField(null=False, blank=True, auto_now_add=True)
