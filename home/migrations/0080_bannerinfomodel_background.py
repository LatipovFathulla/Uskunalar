# Generated by Django 4.0 on 2022-06-21 09:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0079_bannerbackmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='bannerinfomodel',
            name='background',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.bannerbackmodel', verbose_name='background'),
        ),
    ]
