# Generated by Django 4.0 on 2022-07-13 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0087_categorymodel_language_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='categorymodel',
            name='language_code_en',
            field=models.CharField(blank=True, choices=[('RU', 'ru'), ('EN', 'en'), ('UZ', 'uz')], max_length=2, null=True),
        ),
        migrations.AddField(
            model_name='categorymodel',
            name='language_code_ru',
            field=models.CharField(blank=True, choices=[('RU', 'ru'), ('EN', 'en'), ('UZ', 'uz')], max_length=2, null=True),
        ),
        migrations.AddField(
            model_name='categorymodel',
            name='language_code_uz',
            field=models.CharField(blank=True, choices=[('RU', 'ru'), ('EN', 'en'), ('UZ', 'uz')], max_length=2, null=True),
        ),
    ]
