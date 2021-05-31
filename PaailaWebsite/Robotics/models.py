from django.db import models
from django.db.models.fields import BLANK_CHOICE_DASH
from embed_video.fields import EmbedVideoField
from django.urls import reverse
# Create your models here.
class I_1_RoboticsPageTopContent(models.Model):
    title =models.TextField(max_length=100, blank=True)
    description = models.TextField(max_length=100, blank=True)
    youtube_link = EmbedVideoField(max_length=500, blank=True, null=True)

    def __str__(self):
        return "Robotics Page Top Section"

class I_2_RoboticsPageTypeOfRobot(models.Model):
    name_robot = models.TextField(max_length=100, unique=True)
    slug = models.TextField(max_length=100,  unique=True)
    image = models.ImageField(upload_to="photos/robo", blank=True)
    push_imge_to_left = models.BooleanField(default=True)
    title = models.TextField(max_length=100, blank=True)
    description= models.TextField(max_length=500, blank=True)

    def get_url(self):
        return reverse("robot", args=[self.slug])


    def __str__(self):
        return self.name_robot

class I_3_RoboticsPageDeployRobotsSection(models.Model):
    heading = models.TextField(max_length=100, blank=True)
    title = models.TextField(max_length=100, blank=True)
    description = models.TextField(max_length=500, blank=True)
    image = models.ImageField(upload_to="photos/robo", blank=True)
    category_title = models.TextField(max_length=100, blank=True)
    category_description = models.TextField(max_length=500, blank=True)

    def __str__(self):
        return self.category_title




class I_4_RoboticsPageExpertiseSection(models.Model):
    heading = models.TextField(max_length=100, blank=True)
    title = models.TextField(max_length=100, blank=True)
    description = models.TextField(max_length=500, blank=True)
    image = models.ImageField(upload_to="photos/robo", blank=True)
    category_title = models.TextField(max_length=100, blank=True)
    category_description = models.TextField(max_length=500, blank=True)

    def __str__(self):
        return self.category_title



class Z_1_TypeOfRobotPageTopContents(models.Model):
    robot_type = models.OneToOneField(I_2_RoboticsPageTypeOfRobot, on_delete=models.CASCADE)
    title =models.TextField(max_length=100, blank=True)
    description = models.TextField(max_length=500, blank=True)
    
    youtube_link = EmbedVideoField(max_length=500, blank=True, null=True)

    def __str__(self):
        return self.title


class Z_2_TypeOfRobotPageDeployRobot(models.Model):
    robot_type = models.ForeignKey(I_2_RoboticsPageTypeOfRobot, on_delete=models.CASCADE)
    heading = models.TextField(max_length=100, blank=True)
    title = models.TextField(max_length=100, blank=True)
    description = models.TextField(max_length=500, blank=True)
    image = models.ImageField(upload_to="photos/robo", blank=True)
    category_title = models.TextField(max_length=100, blank=True)
    category_description = models.TextField(max_length=500, blank=True)

    def __str__(self):
        return self.category_title

class Z_3_TypeOfRobotEveryThingRobotics(models.Model):
    robot_type = models.ForeignKey(I_2_RoboticsPageTypeOfRobot, on_delete=models.CASCADE)
    heading = models.TextField(max_length=100, blank=True)
    title = models.TextField(max_length=100, blank=True)
    image = models.ImageField(upload_to= "photos/robo", blank = True)
    push_image_to_left = models.BooleanField(default=True)
    category_title = models.TextField(max_length=100, blank=True)
    category_description = models.TextField(max_length=500, blank=True)

    def __str__(self):
        return self.category_title


class Z_4_TypeOfRobotPageHowWeDoIT(models.Model):
    robot_type = models.ForeignKey(I_2_RoboticsPageTypeOfRobot, on_delete=models.CASCADE)
    heading = models.TextField(max_length=100, blank=True)
    title = models.TextField(max_length=100, blank=True)
    description = models.TextField(max_length=500, blank=True)
    image = models.ImageField(upload_to="photos/robo", blank=True)
    category_title = models.TextField(max_length=100, blank=True)
    category_description = models.TextField(max_length=500, blank=True)

    def __str__(self):
        return self.category_title
