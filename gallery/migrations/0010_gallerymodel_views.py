# Generated by Django 4.1.1 on 2023-04-09 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0009_alter_gallerymodel_long_descriptions_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='gallerymodel',
            name='views',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]