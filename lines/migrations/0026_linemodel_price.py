# Generated by Django 4.0 on 2022-07-19 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lines', '0025_alter_linespecificationmodel_line_num_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='linemodel',
            name='price',
            field=models.CharField(max_length=100, null=True, verbose_name='price'),
        ),
    ]
