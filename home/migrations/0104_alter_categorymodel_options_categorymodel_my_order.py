# Generated by Django 4.0 on 2022-07-25 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0103_remove_bannerinfomodel_background_color'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='categorymodel',
            options={'ordering': ['my_order'], 'verbose_name': 'category', 'verbose_name_plural': 'categories'},
        ),
        migrations.AddField(
            model_name='categorymodel',
            name='my_order',
            field=models.PositiveIntegerField(db_index=True, default=0),
        ),
    ]
