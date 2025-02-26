# Generated by Django 4.0 on 2022-03-16 14:07

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('works', '0010_workmodel_descriptions_en_workmodel_descriptions_ru_and_more'),
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
        migrations.AlterField(
            model_name='workmodel',
            name='short_descriptions',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, max_length=520, null=True, verbose_name='short_descriptions'),
        ),
        migrations.AlterField(
            model_name='workmodel',
            name='short_descriptions_en',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, max_length=520, null=True, verbose_name='short_descriptions'),
        ),
        migrations.AlterField(
            model_name='workmodel',
            name='short_descriptions_ru',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, max_length=520, null=True, verbose_name='short_descriptions'),
        ),
        migrations.AlterField(
            model_name='workmodel',
            name='short_descriptions_uz',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, max_length=520, null=True, verbose_name='short_descriptions'),
        ),
    ]
