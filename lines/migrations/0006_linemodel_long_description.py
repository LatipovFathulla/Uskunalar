# Generated by Django 4.0.1 on 2022-02-20 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lines', '0005_remove_linespecificationmodel_line_number_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='linemodel',
            name='long_description',
            field=models.TextField(null=True, verbose_name='long_description'),
        ),
    ]
