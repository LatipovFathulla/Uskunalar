# Generated by Django 4.0 on 2022-07-07 10:10

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion
import embed_video.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GalleryModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300, null=True, verbose_name='title')),
                ('title_uz', models.CharField(max_length=300, null=True, verbose_name='title')),
                ('title_ru', models.CharField(max_length=300, null=True, verbose_name='title')),
                ('title_en', models.CharField(max_length=300, null=True, verbose_name='title')),
                ('short_descriptions', ckeditor_uploader.fields.RichTextUploadingField(null=True, verbose_name='short_description')),
                ('short_descriptions_uz', ckeditor_uploader.fields.RichTextUploadingField(null=True, verbose_name='short_description')),
                ('short_descriptions_ru', ckeditor_uploader.fields.RichTextUploadingField(null=True, verbose_name='short_description')),
                ('short_descriptions_en', ckeditor_uploader.fields.RichTextUploadingField(null=True, verbose_name='short_description')),
                ('long_descriptions', ckeditor_uploader.fields.RichTextUploadingField(null=True, verbose_name='long_description')),
                ('long_descriptions_uz', ckeditor_uploader.fields.RichTextUploadingField(null=True, verbose_name='long_description')),
                ('long_descriptions_ru', ckeditor_uploader.fields.RichTextUploadingField(null=True, verbose_name='long_description')),
                ('long_descriptions_en', ckeditor_uploader.fields.RichTextUploadingField(null=True, verbose_name='long_description')),
                ('last_date', models.DateField(blank=True, null=True, verbose_name='last_date')),
                ('video', embed_video.fields.EmbedVideoField(blank=True, null=True, verbose_name='video')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='created_at')),
            ],
            options={
                'verbose_name': 'gallery',
                'verbose_name_plural': 'galleries',
            },
        ),
        migrations.CreateModel(
            name='GalleyImageModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='gallery_images', verbose_name='image')),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='images', to='gallery.gallerymodel', verbose_name='gallery')),
            ],
            options={
                'verbose_name': 'gallery image',
                'verbose_name_plural': 'gallery images',
            },
        ),
    ]