# Generated by Django 4.0 on 2022-11-21 11:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_blogmodel_views'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blogmodel',
            options={'ordering': ['-pk'], 'verbose_name': 'blog', 'verbose_name_plural': 'blogs'},
        ),
    ]
