from django.db import models
from django.db.models.fields import EmailField

# Create your models here.

class NavFooter(models.Model):
    paaila_black_logo = models.ImageField(upload_to="photos/navbar")
    side_bar_description = models.TextField(max_length=500, blank=True, default='Paaila Technology aims at producing world class human friendly robots that really add value to the business houses that deploy them.')
    side_contact_info_heading = models.CharField(max_length=50, blank=True, default='CONTACT INFO')
    street_address = models.TextField(max_length=100, blank=True, default='Jhamsikhel')
    city =models.TextField(max_length=100, blank=True, default='Lalitpur, Kathmandu')
    email = models.EmailField(blank=True, default='info@paailatechnology.com')
    phone = models.CharField(max_length=25, blank=True, default='+977 015545577')
    learn_more_name1 = models.CharField(max_length=50)
    learn_more_hyperlink1=models.URLField(max_length=500)
    learn_more_name2 = models.CharField(max_length=50)
    learn_more_hyperlink2=models.URLField(max_length=500)
    learn_more_name3 = models.CharField(max_length=50)
    learn_more_hyperlink3=models.URLField(max_length=500)
    learn_more_name4 = models.CharField(max_length=50)
    learn_more_hyperlink4=models.URLField(max_length=500)
    paaila_white_logo = models.ImageField(upload_to="photos/navbar")


    def __str__(self):
        return "Navigation And Footer Information"


class FooterList(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title

class FooterListTitleContents(models.Model):
    footer = models.ForeignKey(FooterList, on_delete=models.CASCADE)
    sub_Title = models.CharField(max_length=50)
    hyperlink = models.URLField(max_length=500)

    def __str__(self):
        return self.sub_Title

class FollowUs(models.Model):
    name_of_media = models.TextField(max_length=50, blank=True)
    font_awesome_class = models.TextField(max_length=100, default='jam jam-twitter')
    hyperlink = models.URLField(max_length=500, blank=True)

    def __str__(self):
        return self.name_of_media