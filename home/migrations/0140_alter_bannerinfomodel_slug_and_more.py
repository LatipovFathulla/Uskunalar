# Generated by Django 4.0 on 2022-10-29 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0139_bannerinfomodel_slug_bannerinfomodel_slug_en_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bannerinfomodel',
            name='slug',
            field=models.SlugField(max_length=400, unique=True),
        ),
        migrations.AlterField(
            model_name='bannerinfomodel',
            name='slug_en',
            field=models.SlugField(max_length=400, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='bannerinfomodel',
            name='slug_ru',
            field=models.SlugField(max_length=400, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='bannerinfomodel',
            name='slug_uz',
            field=models.SlugField(max_length=400, null=True, unique=True),
        ),
    ]
