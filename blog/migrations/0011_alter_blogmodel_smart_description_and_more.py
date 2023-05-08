# Generated by Django 4.1.1 on 2023-05-08 18:26

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_alter_blogmodel_smart_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogmodel',
            name='smart_description',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='smart_description'),
        ),
        migrations.AlterField(
            model_name='blogmodel',
            name='smart_description_en',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='smart_description'),
        ),
        migrations.AlterField(
            model_name='blogmodel',
            name='smart_description_ru',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='smart_description'),
        ),
        migrations.AlterField(
            model_name='blogmodel',
            name='smart_description_uz',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='smart_description'),
        ),
    ]