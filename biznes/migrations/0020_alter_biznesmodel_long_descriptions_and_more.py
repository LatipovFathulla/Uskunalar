# Generated by Django 4.1.1 on 2023-05-08 18:26

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('biznes', '0019_alter_biznesmodel_long_descriptions_and_more'),
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
