from django.db import models
from django.db.models.fields import BLANK_CHOICE_DASH

# Create your models here.


class ICareerSection(models.Model):
    top_image = models.ImageField(upload_to="photos/career", blank =True, null=True)
    top_description = models.CharField(max_length=50, blank =True, null=True)
    top_title = models.CharField(max_length=100, blank=True, default='Work With Us')
    short_note = models.CharField(max_length=100, blank=True, default='A Note On')
    short_note_animated_text =models.CharField(max_length=100, blank=True, default='Our Culture')
    description_of_short_note = models.TextField(blank=True)

    def __str__(self):
        return "Career Section"

class IICurrentOpeningPosition(models.Model):
    position = models.CharField(max_length=100, blank=True, default="Internship")
    location =models.TextField(max_length=300, blank=True, default="Chakupat, Lalitpur, Nepal")
    title = models.TextField(max_length=200, blank=True, default="Software Engineer")
    payment = models.TextField(max_length=300, blank=True, default="Negotiable")
    Deadline = models.TextField(max_length=200, blank=True, default="01/01/20..")
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.position


class IIIWoringWithUs(models.Model):
    heading = models.CharField(max_length=100,default="Benefits of Working With Us", blank=True)
    title =models.CharField(max_length=50, blank=True)
    title_id = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class IVWorkingWithUsContent(models.Model):
    working_with_us = models.ForeignKey(IIIWoringWithUs, default=None ,on_delete=models.CASCADE)
    title = models.CharField(max_length=50, blank=True)
    image = models.ImageField(upload_to="photos/career", blank =True, null=True)
    descriptions = models.TextField(max_length=600, blank=True)

    def __str__(self):
        return self.title


class ResumeSection(models.Model):
    full_name = models.TextField(max_length=100)
    email = models.EmailField()
    address = models.TextField(max_length=100)
    phone = models.TextField(max_length=15)
    resume = models.FileField(upload_to='files', blank=True)
    position = models.TextField(max_length=50,  blank =True, null=True)
    title = models.TextField(max_length=50,  blank =True, null=True)
    strength = models.TextField(max_length=500, blank=True)

    def __str__(self):
        return self.full_name