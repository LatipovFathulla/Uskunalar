# Generated by Django 4.0 on 2022-03-03 09:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0056_alter_bannerinfomodel_secondsubcategory_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bannerinfomodel',
            name='image',
        ),
    ]
