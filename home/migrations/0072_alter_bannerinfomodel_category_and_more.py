# Generated by Django 4.0 on 2022-04-13 09:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0071_alter_categorymodel_category_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bannerinfomodel',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.categorymodel', verbose_name='category'),
        ),
        migrations.AlterField(
            model_name='bannerinfomodel',
            name='category_en',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.categorymodel', verbose_name='category'),
        ),
        migrations.AlterField(
            model_name='bannerinfomodel',
            name='category_ru',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.categorymodel', verbose_name='category'),
        ),
        migrations.AlterField(
            model_name='bannerinfomodel',
            name='category_uz',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.categorymodel', verbose_name='category'),
        ),
    ]
