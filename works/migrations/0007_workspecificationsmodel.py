# Generated by Django 4.0.2 on 2022-02-16 16:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('works', '0006_alter_workmodel_short_descriptions'),
    ]

    operations = [
        migrations.CreateModel(
            name='WorkSpecificationsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('work_customer', models.CharField(max_length=99, verbose_name='work_customer')),
                ('work_number', models.CharField(max_length=99, verbose_name='work_numbers')),
                ('work_image', models.FileField(null=True, upload_to='pdf_image', verbose_name='work_image')),
                ('work', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='work', to='works.workmodel', verbose_name='work')),
            ],
            options={
                'verbose_name': 'product specification',
                'verbose_name_plural': 'product specifications',
            },
        ),
    ]
