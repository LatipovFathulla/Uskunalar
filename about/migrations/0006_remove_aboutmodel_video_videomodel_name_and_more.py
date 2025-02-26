# Generated by Django 4.0.2 on 2022-02-13 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0005_videomodel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aboutmodel',
            name='video',
        ),
        migrations.AddField(
            model_name='videomodel',
            name='name',
            field=models.CharField(max_length=90, null=True, verbose_name='name'),
        ),
        migrations.AddField(
            model_name='videomodel',
            name='video',
            field=models.FileField(null=True, upload_to='about_video', verbose_name='video'),
        ),
        migrations.AddField(
            model_name='videomodel',
            name='video_descriptions',
            field=models.TextField(null=True, verbose_name='video_descriptions'),
        ),
    ]
