from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=50, help_text='e.g: Education')
    biographies = models.ManyToManyField('biographies.Biography', related_name='tags')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
