# Generated by Django 4.1.5 on 2023-02-14 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0019_alter_aboutmodel_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutmodel',
            name='description',
            field=models.TextField(verbose_name='description'),
        ),
        migrations.AlterField(
            model_name='aboutmodel',
            name='description_en',
            field=models.TextField(null=True, verbose_name='description'),
        ),
        migrations.AlterField(
            model_name='aboutmodel',
            name='description_ru',
            field=models.TextField(null=True, verbose_name='description'),
        ),
        migrations.AlterField(
            model_name='aboutmodel',
            name='description_uz',
            field=models.TextField(null=True, verbose_name='description'),
        ),
        migrations.AlterField(
            model_name='aboutmodel',
            name='title',
            field=models.TextField(max_length=90, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='aboutmodel',
            name='title_en',
            field=models.TextField(max_length=90, null=True, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='aboutmodel',
            name='title_ru',
            field=models.TextField(max_length=90, null=True, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='aboutmodel',
            name='title_uz',
            field=models.TextField(max_length=90, null=True, verbose_name='title'),
        ),
    ]