# Generated by Django 4.0 on 2022-04-01 13:14

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0066_alter_bannerinfomodel_sku'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categorymodel',
            name='category',
            field=ckeditor_uploader.fields.RichTextUploadingField(max_length=99, null=True, verbose_name='category'),
        ),
        migrations.AlterField(
            model_name='categorymodel',
            name='category_en',
            field=ckeditor_uploader.fields.RichTextUploadingField(max_length=99, null=True, verbose_name='category'),
        ),
        migrations.AlterField(
            model_name='categorymodel',
            name='category_ru',
            field=ckeditor_uploader.fields.RichTextUploadingField(max_length=99, null=True, verbose_name='category'),
        ),
        migrations.AlterField(
            model_name='categorymodel',
            name='category_uz',
            field=ckeditor_uploader.fields.RichTextUploadingField(max_length=99, null=True, verbose_name='category'),
        ),
    ]
