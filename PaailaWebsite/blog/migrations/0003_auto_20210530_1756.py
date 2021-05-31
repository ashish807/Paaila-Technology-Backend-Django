# Generated by Django 3.2 on 2021-05-30 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20210530_1737'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='author_description',
            field=models.TextField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='blog',
            name='blog_type',
            field=models.TextField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='blog',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]