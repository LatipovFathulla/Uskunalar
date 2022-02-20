# Generated by Django 4.0 on 2022-02-14 10:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0023_alter_categorymodel_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='SpecificationModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=99, verbose_name='title')),
                ('product_customs', models.CharField(max_length=99, null=True, verbose_name='product_customs')),
                ('product_number', models.CharField(max_length=99, null=True, verbose_name='product_number')),
            ],
            options={
                'verbose_name': 'specification',
                'verbose_name_plural': 'specifications',
            },
        ),
        migrations.RemoveField(
            model_name='bannerinfomodel',
            name='product_customs',
        ),
        migrations.RemoveField(
            model_name='bannerinfomodel',
            name='product_number',
        ),
        migrations.AddField(
            model_name='bannerinfomodel',
            name='product_custom',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='home.specificationmodel', verbose_name='product_customs'),
        ),
    ]