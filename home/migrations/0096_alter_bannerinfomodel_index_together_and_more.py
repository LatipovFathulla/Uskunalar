# Generated by Django 4.0 on 2022-07-18 08:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0095_remove_categorymodel_language_code_and_more'),
    ]

    operations = [
        migrations.AlterIndexTogether(
            name='bannerinfomodel',
            index_together={('title', 'category', 'subcategory', 'price')},
        ),
        migrations.RemoveField(
            model_name='bannerinfomodel',
            name='dollar',
        ),
        migrations.RemoveField(
            model_name='bannerinfomodel',
            name='image',
        ),
    ]
