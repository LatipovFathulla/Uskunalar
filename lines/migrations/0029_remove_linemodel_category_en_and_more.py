# Generated by Django 4.0 on 2022-09-24 12:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lines', '0028_linemodel_views'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='linemodel',
            name='category_en',
        ),
        migrations.RemoveField(
            model_name='linemodel',
            name='category_ru',
        ),
        migrations.RemoveField(
            model_name='linemodel',
            name='category_uz',
        ),
    ]