# Generated by Django 4.0 on 2022-11-02 20:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('biznes', '0017_rename_biznes_views_biznesmodel_views'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='biznesmodel',
            options={'ordering': ['-pk'], 'verbose_name': 'biznes', 'verbose_name_plural': 'biznes'},
        ),
    ]
