# Generated by Django 4.0 on 2022-07-16 07:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0094_remove_productspecificationsmodel_language_code'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='categorymodel',
            name='language_code',
        ),
        migrations.RemoveField(
            model_name='categorymodel',
            name='language_code_en',
        ),
        migrations.RemoveField(
            model_name='categorymodel',
            name='language_code_ru',
        ),
        migrations.RemoveField(
            model_name='categorymodel',
            name='language_code_uz',
        ),
        migrations.RemoveField(
            model_name='subcategorymodel',
            name='language_code',
        ),
        migrations.RemoveField(
            model_name='subcategorymodel',
            name='language_code_en',
        ),
        migrations.RemoveField(
            model_name='subcategorymodel',
            name='language_code_ru',
        ),
        migrations.RemoveField(
            model_name='subcategorymodel',
            name='language_code_uz',
        ),
    ]
