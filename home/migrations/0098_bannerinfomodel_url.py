# Generated by Django 4.0 on 2022-07-20 07:08

from django.db import migrations
import embed_video.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0097_alter_bannerinfomodel_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='bannerinfomodel',
            name='url',
            field=embed_video.fields.EmbedVideoField(null=True),
        ),
    ]
