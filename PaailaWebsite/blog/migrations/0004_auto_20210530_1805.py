# Generated by Django 3.2 on 2021-05-30 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20210530_1756'),
    ]

    operations = [
        migrations.CreateModel(
            name='TopBlogPage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blog_top_image', models.ImageField(blank=True, upload_to='photos/blog')),
                ('blog_top_title', models.TextField(default='BLOG PAGE', max_length=100)),
                ('blog_top_description', models.TextField(default='Paaila Technology', max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='blog',
            name='blog_top_description',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='blog_top_image',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='blog_top_title',
        ),
    ]