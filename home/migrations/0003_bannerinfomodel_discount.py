# Generated by Django 4.0 on 2021-12-24 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_errormodel_alter_singlebannermodel_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='bannerinfomodel',
            name='discount',
            field=models.PositiveIntegerField(default=0, verbose_name='discount'),
        ),
    ]
