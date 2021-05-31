from django.db import models
from django.db.models.fields.files import ImageField
from ckeditor.fields import RichTextField
from django.urls import reverse
from embed_video.fields import EmbedVideoField
# Create your models here.


class ArtificialIntellience(models.Model):
    title = models.CharField(max_length=100, blank=True)
    description = RichTextField(blank=True)
    video = EmbedVideoField(max_length=500, blank=True, null=True)
    description_after_video = models.TextField(max_length=500, blank=True)
    heading = models.CharField(max_length=100, blank=True)
    more_details = RichTextField(blank=True)

    def __str__(self):
        return "Artificial Intellience Section"

class ServicesList(models.Model):
    image = models.ImageField(upload_to = 'photos/ai')
    title = models.CharField(max_length=100, blank=True)
    description = models.TextField(max_length=300, blank=True)
    button_name = models.CharField(max_length=50, default='Learn More')
    hyperlink = models.URLField(max_length=500, blank=True)

    def __str__(self):
        return self.title