# Generated by Django 4.0 on 2022-02-14 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0021_remove_bannerinfomodel_error_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='categorymodel',
            name='image',
            field=models.ImageField(null=True, upload_to='category_image', verbose_name='category_image'),
        ),
    ]