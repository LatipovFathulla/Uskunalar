# Generated by Django 4.0.1 on 2022-02-20 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_blogmodel_smart_description_blogmodel_smart_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogmodel',
            name='smart_description',
            field=models.TextField(blank=True, null=True, verbose_name='smart_description'),
        ),
    ]