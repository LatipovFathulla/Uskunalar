# Generated by Django 4.0 on 2022-07-07 10:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0002_gallerymodel_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gallerymodel',
            name='name',
        ),
    ]
