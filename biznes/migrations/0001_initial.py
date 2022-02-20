# Generated by Django 4.0.1 on 2022-02-20 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BiznesModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='title')),
                ('image', models.FileField(upload_to='biznes', verbose_name='biznes_image')),
                ('long_descriptions', models.TextField(verbose_name='long_descriptions')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created_at')),
            ],
            options={
                'verbose_name': 'biznes',
                'verbose_name_plural': 'biznes',
            },
        ),
    ]