# Generated by Django 4.0 on 2022-03-16 14:07

from django.db import migrations
import embed_video.fields


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0015_alter_aboutmodel_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutmodel',
            name='url',
            field=embed_video.fields.EmbedVideoField(blank=True, null=True),
        ),
    ]
