# Generated by Django 4.0 on 2022-07-13 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0086_alter_bannerinfomodel_city_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='categorymodel',
            name='language_code',
            field=models.CharField(blank=True, choices=[('RU', 'ru'), ('EN', 'en'), ('UZ', 'uz')], max_length=2, null=True),
        ),
    ]
