from django.db import models
from django.utils import timezone


class Biography(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='biographies',
                              help_text="image landscape size 400px * 200px")
    url_target = models.CharField(max_length=256, blank=True)
    position = models.PositiveIntegerField(blank=True, null=True)
    short_description = models.TextField(default='', blank=True)
    description = models.TextField()
    created = models.DateTimeField(default=timezone.localtime)

    def __str__(self):
        return self.title
