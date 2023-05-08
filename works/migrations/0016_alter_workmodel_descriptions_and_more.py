# Generated by Django 4.1.1 on 2023-05-08 18:26

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('works', '0015_workmodel_views'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workmodel',
            name='descriptions',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='descriptions'),
        ),
        migrations.AlterField(
            model_name='workmodel',
            name='descriptions_en',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='descriptions'),
        ),
        migrations.AlterField(
            model_name='workmodel',
            name='descriptions_ru',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='descriptions'),
        ),
        migrations.AlterField(
            model_name='workmodel',
            name='descriptions_uz',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='descriptions'),
        ),
    ]
