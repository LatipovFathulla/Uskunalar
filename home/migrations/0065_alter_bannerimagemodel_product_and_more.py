# Generated by Django 4.0 on 2022-03-16 14:07

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0064_alter_secondsubcategorymodel_category_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bannerimagemodel',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='images', to='home.bannerinfomodel', verbose_name='product'),
        ),
        migrations.AlterField(
            model_name='bannerinfomodel',
            name='long_description',
            field=ckeditor_uploader.fields.RichTextUploadingField(null=True, verbose_name='long_description'),
        ),
        migrations.AlterField(
            model_name='bannerinfomodel',
            name='pdf',
            field=models.FileField(blank=True, null=True, upload_to='pdf', verbose_name='pdf'),
        ),
        migrations.AlterField(
            model_name='bannerinfomodel',
            name='short_description',
            field=ckeditor_uploader.fields.RichTextUploadingField(null=True, verbose_name='short_description'),
        ),
        migrations.AlterField(
            model_name='categorymodel',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to='category_image', verbose_name='category_image'),
        ),
        migrations.AlterField(
            model_name='productspecificationsmodel',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='specifications', to='home.bannerinfomodel', verbose_name='products'),
        ),
        migrations.AlterField(
            model_name='productspecificationsmodel',
            name='product_customer',
            field=models.CharField(blank=True, max_length=99, null=True, verbose_name='product_customer'),
        ),
        migrations.AlterField(
            model_name='productspecificationsmodel',
            name='product_number',
            field=models.CharField(blank=True, max_length=99, null=True, verbose_name='product_numbers'),
        ),
        migrations.AlterField(
            model_name='subcategorymodel',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to='sub_image', verbose_name='sub_image'),
        ),
    ]