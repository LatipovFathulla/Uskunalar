# Generated by Django 4.0 on 2022-09-29 13:59

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0126_remove_bannerinfomodel_sent_bannerinfomodel_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bannerinfomodel',
            name='type',
        ),
        migrations.AddField(
            model_name='bannerinfomodel',
            name='priceType',
            field=ckeditor_uploader.fields.RichTextUploadingField(null=True, verbose_name='priceType'),
        ),
        migrations.DeleteModel(
            name='ProductEXWModel',
        ),
    ]
