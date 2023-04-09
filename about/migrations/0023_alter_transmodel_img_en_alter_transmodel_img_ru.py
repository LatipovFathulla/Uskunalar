# Generated by Django 4.1.1 on 2023-03-17 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0022_transmodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transmodel',
            name='img_en',
            field=models.FileField(upload_to='banner_image_en', verbose_name='img_en'),
        ),
        migrations.AlterField(
            model_name='transmodel',
            name='img_ru',
            field=models.FileField(upload_to='banner_image_ru', verbose_name='img_ru'),
        ),
    ]