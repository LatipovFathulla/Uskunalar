# Generated by Django 4.0 on 2021-12-25 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_alter_secondsubcategorymodel_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='singlebannermodel',
            name='banner_price',
            field=models.IntegerField(null=True, verbose_name='banner_price'),
        ),
        migrations.AlterField(
            model_name='singlebannermodel',
            name='banner_price_dollar',
            field=models.IntegerField(null=True, verbose_name='banner_price_dollar'),
        ),
        migrations.AlterField(
            model_name='singlebannermodel',
            name='banner_sku',
            field=models.IntegerField(null=True, verbose_name='banner_sku'),
        ),
        migrations.AlterField(
            model_name='singlebannermodel',
            name='banner_title',
            field=models.CharField(max_length=99, null=True, verbose_name='banner_title'),
        ),
    ]