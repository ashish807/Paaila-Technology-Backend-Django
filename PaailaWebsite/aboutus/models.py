from django.db import models
from django.db.models.fields import BLANK_CHOICE_DASH

# Create your models here.


class IAboutUSSection(models.Model):
    top_image = models.ImageField(upload_to = 'photos/about')
    top_title = models.TextField(max_length=100, blank=True)
    top_sub_title = models.TextField(max_length=150, blank=True)

    def __str__(self):
        return "About Top Section"


class IIAboutTextImageAlterSection(models.Model):
    image = models.ImageField(upload_to = 'photos/about')
    push_image_to_left = models.BooleanField(default=True)
    title = models.TextField(max_length=200, blank=True)
    description = models.TextField(max_length=600, blank=True)
    button_name = models.CharField(max_length=100, default='More Details')
    hyperlink = models.URLField(blank=True, max_length=500)
    
    def __str__(self):
        return self.title



class IIICompanyProgress(models.Model):
    heading = models.CharField(max_length=100, default='Company Progress', blank=True)
    percentage_progress = models.IntegerField()
    title = models.CharField(max_length=100, blank=True)
    description = models.TextField(max_length=150, blank=True)

    def __str__(self):
        return self.title



class IVWorkingSteps(models.Model):
    heading = models.TextField(max_length=150, blank=True)
    image = models.ImageField(upload_to='photos/about', blank=True)
    title = models.CharField(max_length=100, blank=True)
    description = models.TextField(max_length=150, blank=True)

    def __str__(self):
        return self.title


class VTeamBox(models.Model):
    heading = models.TextField(max_length=100, blank=True, default="Team Members")
    name = models.CharField(max_length=100, blank=True, default='Team Memebers name')
    image = models.ImageField(upload_to = 'photos/about', blank=True)
    designation = models.CharField(max_length=100, blank=True)
    description = models.TextField(max_length=150, blank =True)
    twitter_link = models.URLField(max_length=500, blank=True)
    facebook_link = models.URLField(max_length=500, blank=True)
    instagram_link = models.URLField(max_length=500,blank=True)

    def __str__(self):
        return self.name

class VISubscribe(models.Model):
    heading = models.TextField(max_length=200, blank=True, default='Subscribe to our newsletter to get our news and deals delivered to your inbox!')
    image = models.ImageField(upload_to="photos/about", blank=True)
    button_name = models.CharField(max_length=50, blank=True)
    hyperlink = models.CharField(max_length=500, blank=True)


    def __str__(self):
        return "Subscribe Section"