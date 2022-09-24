# Generated by Django 4.0 on 2022-09-24 13:02

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0121_remove_bannerinfomodel_subcategory_en_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bannerinfomodel',
            name='short_description',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='short_description'),
        ),
        migrations.AlterField(
            model_name='bannerinfomodel',
            name='short_description_en',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='short_description'),
        ),
        migrations.AlterField(
            model_name='bannerinfomodel',
            name='short_description_ru',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='short_description'),
        ),
        migrations.AlterField(
            model_name='bannerinfomodel',
            name='short_description_uz',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='short_description'),
        ),
    ]
