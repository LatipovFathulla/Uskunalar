# Generated by Django 4.0 on 2022-04-04 12:39

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lines', '0018_alter_linecategorymodel_category_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='linecategorymodel',
            name='category',
            field=ckeditor_uploader.fields.RichTextUploadingField(max_length=100, verbose_name='category'),
        ),
        migrations.AlterField(
            model_name='linecategorymodel',
            name='category_en',
            field=ckeditor_uploader.fields.RichTextUploadingField(max_length=100, null=True, verbose_name='category'),
        ),
        migrations.AlterField(
            model_name='linecategorymodel',
            name='category_ru',
            field=ckeditor_uploader.fields.RichTextUploadingField(max_length=100, null=True, verbose_name='category'),
        ),
        migrations.AlterField(
            model_name='linecategorymodel',
            name='category_uz',
            field=ckeditor_uploader.fields.RichTextUploadingField(max_length=100, null=True, verbose_name='category'),
        ),
    ]