# Generated by Django 4.0 on 2022-04-14 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('watermarker', '0002_auto_20210320_2145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='watermark',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
