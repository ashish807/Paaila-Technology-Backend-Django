# Generated by Django 3.2 on 2021-06-01 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatbot', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='iiicustomerusingourchatbot',
            old_name='title',
            new_name='title_1',
        ),
        migrations.AddField(
            model_name='iiicustomerusingourchatbot',
            name='title_2',
            field=models.TextField(blank=True, max_length=200),
        ),
    ]
