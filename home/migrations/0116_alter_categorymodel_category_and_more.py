# Generated by Django 4.0 on 2022-09-16 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0115_alter_bannerinfomodel_category_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categorymodel',
            name='category',
            field=models.CharField(db_index=True, max_length=400, null=True, verbose_name='category'),
        ),
        migrations.AlterField(
            model_name='categorymodel',
            name='category_en',
            field=models.CharField(db_index=True, max_length=400, null=True, verbose_name='category'),
        ),
        migrations.AlterField(
            model_name='categorymodel',
            name='category_ru',
            field=models.CharField(db_index=True, max_length=400, null=True, verbose_name='category'),
        ),
        migrations.AlterField(
            model_name='categorymodel',
            name='category_uz',
            field=models.CharField(db_index=True, max_length=400, null=True, verbose_name='category'),
        ),
    ]
