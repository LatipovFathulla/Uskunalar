# Generated by Django 4.0 on 2022-07-07 10:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0005_galleyimagemodel_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='galleyimagemodel',
            name='image',
        ),
    ]