# Generated by Django 3.2 on 2021-05-29 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Career', '0002_ivworkingwithuscontent'),
    ]

    operations = [
        migrations.AddField(
            model_name='ivworkingwithuscontent',
            name='title',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
