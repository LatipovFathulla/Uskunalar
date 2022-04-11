# Generated by Django 4.0 on 2022-04-05 19:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('biznes', '0005_remove_biznesimagemodel_work_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='biznesimagemodel',
            name='biznes_image',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='biznes_image', to='biznes.biznesmodel', verbose_name='biznes_image'),
        ),
        migrations.AlterField(
            model_name='biznesimagemodel',
            name='biznes_num',
            field=models.CharField(max_length=200, verbose_name='biznes_num'),
        ),
        migrations.AlterField(
            model_name='biznesimagemodel',
            name='biznes_spec',
            field=models.CharField(max_length=200, verbose_name='biznes_spec'),
        ),
        migrations.AlterField(
            model_name='biznesimagemodel',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='created_at'),
        ),
    ]