# Generated by Django 4.0 on 2022-10-27 10:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0137_alter_bannerinfomodel_delivery_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bannerinfomodel',
            options={'ordering': ['-pk'], 'verbose_name': 'products', 'verbose_name_plural': 'products'},
        ),
    ]
