# Generated by Django 4.0 on 2022-06-06 09:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0076_bannerinfomodel_delivery_en_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bannerinfomodel',
            name='secondsubcategory',
        ),
        migrations.RemoveField(
            model_name='bannerinfomodel',
            name='secondsubcategory_en',
        ),
        migrations.RemoveField(
            model_name='bannerinfomodel',
            name='secondsubcategory_ru',
        ),
        migrations.RemoveField(
            model_name='bannerinfomodel',
            name='secondsubcategory_uz',
        ),
        migrations.DeleteModel(
            name='SecondSubCategoryModel',
        ),
    ]
