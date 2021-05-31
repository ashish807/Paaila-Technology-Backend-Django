from django.db import models
from ckeditor.fields import RichTextField
from django.urls import reverse
from embed_video.fields import EmbedVideoField

# Create your models here.
class TopBlogPage(models.Model):
    blog_top_image = models.ImageField(upload_to="photos/blog", blank=True)
    blog_top_title = models.TextField(max_length=100,  default="BLOG PAGE")

    blog_top_description = models.TextField(max_length=100,  default="Paaila Technology")

    def __str__(self):
        return "Blog Top Content"
        
class Blog(models.Model):
    image = models.ImageField(upload_to="photos/blog", blank=True)
    title = models.TextField(max_length=100,  unique=True)
    slug = models.TextField(max_length=100,  unique=True)
    blog_type = models.TextField(max_length=50, blank=True)
    short_description = models.TextField(max_length=100)
    description = RichTextField(blank=True)
    youtube_video=EmbedVideoField(max_length=500, blank=True, null=True)
    author_image =    models.ImageField(upload_to="photos/blog", blank=True)
    author_name = models.TextField(max_length=100, blank=True)
    author_description =models.TextField(max_length=100, blank=True) 
    created_date      = models.DateTimeField(auto_now_add=True)
    modified_date     = models.DateField(auto_now=True)


    def get_url(self):
        return reverse("blog_content", args=[self.slug])


    def __str__(self):
        return self.title




class BlogComment(models.Model):
    blog        = models.ForeignKey(Blog, on_delete=models.CASCADE)
    name        = models.CharField(max_length=100)
    phone       = models.CharField(max_length=15)
    email       = models.EmailField()
    comment     = models.TextField(max_length=500)
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name