# Generated by Django 4.0 on 2022-06-21 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0080_bannerinfomodel_background'),
    ]

    operations = [
        migrations.AddField(
            model_name='bannerbackmodel',
            name='color',
            field=models.CharField(db_index=True, max_length=99, null=True, verbose_name='color'),
        ),
    ]
