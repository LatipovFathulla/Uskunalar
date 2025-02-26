# Generated by Django 4.0 on 2022-03-16 13:53

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0014_alter_requestsmodel_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutmodel',
            name='description',
            field=ckeditor_uploader.fields.RichTextUploadingField(verbose_name='description'),
        ),
        migrations.AlterField(
            model_name='aboutmodel',
            name='description_en',
            field=ckeditor_uploader.fields.RichTextUploadingField(null=True, verbose_name='description'),
        ),
        migrations.AlterField(
            model_name='aboutmodel',
            name='description_ru',
            field=ckeditor_uploader.fields.RichTextUploadingField(null=True, verbose_name='description'),
        ),
        migrations.AlterField(
            model_name='aboutmodel',
            name='description_uz',
            field=ckeditor_uploader.fields.RichTextUploadingField(null=True, verbose_name='description'),
        ),
    ]
