# Generated by Django 4.0.2 on 2022-02-16 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('works', '0005_alter_workmodel_short_descriptions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workmodel',
            name='short_descriptions',
            field=models.TextField(max_length=520, null=True, verbose_name='short_descriptions'),
        ),
    ]
