# Generated by Django 4.0 on 2021-12-24 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_alter_bannerinfomodel_price_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bannerinfomodel',
            name='discount',
            field=models.PositiveIntegerField(default=0, verbose_name='discount'),
        ),
        migrations.AlterField(
            model_name='bannerinfomodel',
            name='price',
            field=models.IntegerField(null=True, verbose_name='price'),
        ),
        migrations.AlterField(
            model_name='bannerinfomodel',
            name='price_dollar',
            field=models.IntegerField(null=True, verbose_name='price_dollar'),
        ),
    ]
