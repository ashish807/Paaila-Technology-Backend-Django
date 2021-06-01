from django.db import models

# Create your models here.
# Create your models here.
class ISlidingScreenShotImage(models.Model):
    image=models.ImageField(upload_to="photos/chatbot")
    heading= models.TextField(max_length=200, blank=True)
    description= models.TextField(max_length=200, blank=True)
    def __str__(self):
        return self.heading

class IIAdvertising(models.Model):
    image=models.ImageField(upload_to="photos/chatbot")
    title = models.TextField(max_length=150, blank=True)
    point1 =models.TextField(max_length=150, blank=True)
    point2=models.TextField(max_length=150, blank=True)
    point3=models.TextField(max_length=150, blank=True)
    point4=models.TextField(max_length=150, blank=True)
    benefit_for =models.TextField(max_length=150, blank=True)

    def __str__(self):
        return self.title


class IIICustomerUsingOurChatBot(models.Model):
    title_1 = models.TextField(max_length=200, blank=True)
    title_2 = models.TextField(max_length=200, blank=True)
    name_company = models.TextField(max_length=200, blank=True)
    image = models.ImageField(upload_to="photos/chatbot")

    def __str__(self) :
        return self.name_company

class IVSecondAdvertising(models.Model):
    title_1 = models.TextField(max_length=150, blank=True)
    title_2=models.TextField(max_length=150, blank=True)
    description_1=models.TextField(max_length=300, blank=True)
    description_2=models.TextField(max_length=150, blank=True)
    image_1 =models.ImageField(upload_to="photos/chatbot")
    image_title_1=models.TextField(max_length=150, blank=True)
    image_description_1=models.TextField(max_length=150, blank=True)
    slogan_1 = models.TextField(max_length=150, blank=True)
    image_2 =models.ImageField(upload_to="photos/chatbot")
    image_title_2=models.TextField(max_length=150, blank=True)
    image_description_2=models.TextField(max_length=150, blank=True)
    slogan_2 = models.TextField(max_length=150, blank=True)

    def __str__(self):
        return self.title_1