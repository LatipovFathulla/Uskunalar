# Generated by Django 4.0 on 2022-02-25 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0010_rename_contactmodel_requestsmodel_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutmodel',
            name='long_description',
            field=models.TextField(null=True, verbose_name='long_description'),
        ),
    ]
