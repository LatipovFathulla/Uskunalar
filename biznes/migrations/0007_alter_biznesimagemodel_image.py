# Generated by Django 4.0 on 2022-04-05 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biznes', '0006_alter_biznesimagemodel_biznes_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='biznesimagemodel',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to='biznes_single', verbose_name='biznes_image'),
        ),
    ]