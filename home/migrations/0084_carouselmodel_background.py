# Generated by Django 4.0 on 2022-06-29 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0083_alter_bannerinfomodel_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='carouselmodel',
            name='background',
            field=models.FileField(null=True, upload_to='Banner_background', verbose_name='background'),
        ),
    ]
