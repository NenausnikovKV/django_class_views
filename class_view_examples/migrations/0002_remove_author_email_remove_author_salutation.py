# Generated by Django 5.0.1 on 2024-01-25 11:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('class_view_examples', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='email',
        ),
        migrations.RemoveField(
            model_name='author',
            name='salutation',
        ),
    ]
