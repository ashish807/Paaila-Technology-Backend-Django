from django.db import models

# Create your models here.
class ISlidingImage(models.Model):
    image=models.ImageField(upload_to="photos/home")
    heading= models.TextField(max_length=200, blank=True)
    description= models.TextField(max_length=200, blank=True)
    button_name= models.TextField(max_length=200, blank=True, default='See Our Project')
    button_hyperlink=models.TextField(max_length=500, blank=True)

    def __str__(self):
        return self.heading

class IIQuantityTitle(models.Model):
    quantity=models.IntegerField(blank=True)
    title=models.TextField(max_length=100, blank=True)

    def __str__(self):
        return self.title

class IIIApplicationArea(models.Model):
    title=models.TextField(max_length=100, blank=True)
    image=models.ImageField(upload_to="photos/home")
    description=models.TextField(max_length=100, blank=True)
    def _str_(self):
        return self.description



class IVMediaCoverage(models.Model):
    title=models.TextField(max_length=100, blank=True)
    media_name =models.TextField(max_length=100, blank=True)
    logo=models.ImageField(upload_to="photos/home", null=True)
    date=models.CharField(max_length=100)
    heading=models.TextField(max_length=150)
    hyperlink_name=models.TextField(max_length=100, blank=True)
    hyperlink=models.URLField(max_length = 500,blank=True,null=True)
    #hyperlink

    def __str__(self):
        return self.heading



class VCompaniesLoveList(models.Model):
    company_name=models.TextField(max_length=150,blank=True)
    logo_name=models.TextField(max_length=150,blank=True)
    logo=models.ImageField(upload_to="photos/home")

    def __str__(self):
        return self.logo_name
