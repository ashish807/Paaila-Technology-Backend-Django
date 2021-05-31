from django.db import models
from django.db.models.fields import URLField

# Create your models here.


class BasicInfoSection(models.Model):
    twitter_link = models.URLField(max_length=500, blank=True)
    faceboo_link = models.URLField(max_length=500, blank=True)
    instagram_link = models.URLField(max_length=500, blank=True)
    youtube_link = models.URLField(max_length=500, blank=True)
    address_line_1 = models.TextField(max_length=50, blank=True)
    address_line_2 = models.TextField(max_length=50, blank=True)
    city = models.TextField(max_length=50, blank=True)
    state = models.TextField(max_length=50, blank=True)
    country = models.TextField(max_length=50, blank=True)
    phone = models.TextField(max_length=50, blank=True)
    email = models.EmailField(blank=True)
    
    def full_address(self):
        return f'{self.address_line_1} {self.address_line_2}'
    def __str__(self):
        return "Basic Info"
    
class ContactUsSection(models.Model):
    title = models.CharField(max_length=100, blank=True, default="Contact Us")
    image = models.ImageField(upload_to = "photos/contact", blank=True)

    def __str__(self):
        return "Contact Us Section"



