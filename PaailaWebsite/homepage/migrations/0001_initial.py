# Generated by Django 3.2 on 2021-05-26 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='IIIApplicationArea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(blank=True, max_length=100)),
                ('image', models.ImageField(upload_to='photos/home')),
                ('description', models.TextField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='IIQuantityTitle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(blank=True)),
                ('title', models.TextField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ISlidingImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='photos/home')),
                ('heading', models.TextField(blank=True, max_length=200)),
                ('description', models.TextField(blank=True, max_length=200)),
                ('button_name', models.TextField(blank=True, max_length=200)),
                ('button_hyperlink', models.TextField(blank=True, max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='IVMediaCoverage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(blank=True, max_length=100)),
                ('media_name', models.TextField(blank=True, max_length=100)),
                ('logo', models.ImageField(null=True, upload_to='photos/home')),
                ('date', models.CharField(max_length=100)),
                ('heading', models.TextField(max_length=150)),
                ('hyperlink_name', models.TextField(blank=True, max_length=100)),
                ('hyperlink', models.URLField(blank=True, max_length=500, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='VCompaniesLoveList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.TextField(blank=True, max_length=150)),
                ('logo_name', models.TextField(blank=True, max_length=150)),
                ('logo', models.ImageField(upload_to='photos/home')),
            ],
        ),
    ]