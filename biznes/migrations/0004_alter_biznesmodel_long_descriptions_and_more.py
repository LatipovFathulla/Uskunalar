# Generated by Django 4.0 on 2022-03-16 14:07

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('biznes', '0003_biznesmodel_long_descriptions_en_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='biznesmodel',
            name='long_descriptions',
            field=ckeditor_uploader.fields.RichTextUploadingField(verbose_name='long_descriptions'),
        ),
        migrations.AlterField(
            model_name='biznesmodel',
            name='long_descriptions_en',
            field=ckeditor_uploader.fields.RichTextUploadingField(null=True, verbose_name='long_descriptions'),
        ),
        migrations.AlterField(
            model_name='biznesmodel',
            name='long_descriptions_ru',
            field=ckeditor_uploader.fields.RichTextUploadingField(null=True, verbose_name='long_descriptions'),
        ),
        migrations.AlterField(
            model_name='biznesmodel',
            name='long_descriptions_uz',
            field=ckeditor_uploader.fields.RichTextUploadingField(null=True, verbose_name='long_descriptions'),
        ),
    ]
