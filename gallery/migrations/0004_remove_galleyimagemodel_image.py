# Generated by Django 4.0 on 2022-07-07 10:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0003_remove_gallerymodel_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='galleyimagemodel',
            name='image',
        ),
    ]