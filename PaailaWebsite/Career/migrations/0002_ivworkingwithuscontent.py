# Generated by Django 3.2 on 2021-05-29 07:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Career', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='IVWorkingWithUsContent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descriptions', models.TextField(blank=True, max_length=600)),
                ('working_with_us', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='Career.iiiworingwithus')),
            ],
        ),
    ]
