# Generated by Django 4.0 on 2022-02-17 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_blogmodel_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogmodel',
            name='smart_description',
            field=models.TextField(blank=True, null=True, verbose_name='smart_decoration'),
        ),
        migrations.AddField(
            model_name='blogmodel',
            name='smart_text',
            field=models.TextField(blank=True, null=True, verbose_name='smart_text'),
        ),
    ]
