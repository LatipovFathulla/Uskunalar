# Generated by Django 4.0 on 2022-10-02 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_alter_blogmodel_description_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogmodel',
            name='smart_text',
        ),
        migrations.RemoveField(
            model_name='blogmodel',
            name='smart_text_en',
        ),
        migrations.RemoveField(
            model_name='blogmodel',
            name='smart_text_ru',
        ),
        migrations.RemoveField(
            model_name='blogmodel',
            name='smart_text_uz',
        ),
        migrations.AlterField(
            model_name='blogmodel',
            name='description',
            field=models.TextField(null=True, verbose_name='description'),
        ),
        migrations.AlterField(
            model_name='blogmodel',
            name='description_en',
            field=models.TextField(null=True, verbose_name='description'),
        ),
        migrations.AlterField(
            model_name='blogmodel',
            name='description_ru',
            field=models.TextField(null=True, verbose_name='description'),
        ),
        migrations.AlterField(
            model_name='blogmodel',
            name='description_uz',
            field=models.TextField(null=True, verbose_name='description'),
        ),
    ]
