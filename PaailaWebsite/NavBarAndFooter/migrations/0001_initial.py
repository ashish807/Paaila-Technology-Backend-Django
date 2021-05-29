# Generated by Django 3.2 on 2021-05-26 19:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FollowUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_of_media', models.TextField(blank=True, max_length=50)),
                ('font_awesome_class', models.TextField(default='jam jam-twitter', max_length=100)),
                ('hyperlink', models.URLField(blank=True, max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='FooterList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='NavFooter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paaila_black_logo', models.ImageField(upload_to='photos/navbar')),
                ('side_bar_description', models.TextField(blank=True, default='Paaila Technology aims at producing world class human friendly robots that really add value to the business houses that deploy them.', max_length=500)),
                ('side_contact_info_heading', models.CharField(blank=True, default='CONTACT INFO', max_length=50)),
                ('street_address', models.TextField(blank=True, default='Jhamsikhel', max_length=100)),
                ('city', models.TextField(blank=True, default='Lalitpur, Kathmandu', max_length=100)),
                ('email', models.EmailField(blank=True, default='info@paailatechnology.com', max_length=254)),
                ('phone', models.CharField(blank=True, default='+977 015545577', max_length=25)),
                ('learn_more_name1', models.CharField(max_length=50)),
                ('learn_more_hyperlink1', models.URLField(max_length=500)),
                ('learn_more_name2', models.CharField(max_length=50)),
                ('learn_more_hyperlink2', models.URLField(max_length=500)),
                ('learn_more_name3', models.CharField(max_length=50)),
                ('learn_more_hyperlink3', models.URLField(max_length=500)),
                ('learn_more_name4', models.CharField(max_length=50)),
                ('learn_more_hyperlink4', models.URLField(max_length=500)),
                ('paaila_white_logo', models.ImageField(upload_to='photos/navbar')),
            ],
        ),
        migrations.CreateModel(
            name='FooterListTitleContents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_Title', models.CharField(max_length=50)),
                ('hyperlink', models.URLField(max_length=500)),
                ('footer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='NavBarAndFooter.footerlist')),
            ],
        ),
    ]
