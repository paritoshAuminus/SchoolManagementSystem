from django.db import models

# Create your models here.
class School(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(default=None, null=True, blank=True)
    image = models.ImageField(upload_to='images/', default=None, null=True, blank=True)

    def __str__(self):
        return self.title

