# Generated by Django 4.0.2 on 2022-02-16 18:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('works', '0008_alter_workspecificationsmodel_work_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='workspecificationsmodel',
            options={'verbose_name': 'work specification', 'verbose_name_plural': 'work specifications'},
        ),
        migrations.CreateModel(
            name='WorkImageModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(upload_to='work_single', verbose_name='work_image')),
                ('work_image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='work_image', to='works.workmodel', verbose_name='work_image')),
            ],
            options={
                'verbose_name': 'work_image',
                'verbose_name_plural': 'work_image',
            },
        ),
    ]