# Generated by Django 4.0 on 2022-04-05 19:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('biznes', '0004_alter_biznesmodel_long_descriptions_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='biznesimagemodel',
            name='work_image',
        ),
        migrations.AddField(
            model_name='biznesimagemodel',
            name='biznes_image',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='biznes_image', to='biznes.biznesmodel', verbose_name='biznes_image'),
        ),
        migrations.AddField(
            model_name='biznesimagemodel',
            name='biznes_num',
            field=models.CharField(max_length=200, null=True, verbose_name='biznes_num'),
        ),
        migrations.AddField(
            model_name='biznesimagemodel',
            name='biznes_spec',
            field=models.CharField(max_length=200, null=True, verbose_name='biznes_spec'),
        ),
        migrations.AddField(
            model_name='biznesimagemodel',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='created_at'),
        ),
    ]
