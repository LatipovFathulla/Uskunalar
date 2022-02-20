# Generated by Django 4.0 on 2022-02-14 11:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0028_bannerinfomodel_product_customs10_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bannerinfomodel',
            name='product_customs',
        ),
        migrations.RemoveField(
            model_name='bannerinfomodel',
            name='product_customs10',
        ),
        migrations.RemoveField(
            model_name='bannerinfomodel',
            name='product_customs11',
        ),
        migrations.RemoveField(
            model_name='bannerinfomodel',
            name='product_customs12',
        ),
        migrations.RemoveField(
            model_name='bannerinfomodel',
            name='product_customs2',
        ),
        migrations.RemoveField(
            model_name='bannerinfomodel',
            name='product_customs3',
        ),
        migrations.RemoveField(
            model_name='bannerinfomodel',
            name='product_customs4',
        ),
        migrations.RemoveField(
            model_name='bannerinfomodel',
            name='product_customs5',
        ),
        migrations.RemoveField(
            model_name='bannerinfomodel',
            name='product_customs6',
        ),
        migrations.RemoveField(
            model_name='bannerinfomodel',
            name='product_customs7',
        ),
        migrations.RemoveField(
            model_name='bannerinfomodel',
            name='product_customs8',
        ),
        migrations.RemoveField(
            model_name='bannerinfomodel',
            name='product_customs9',
        ),
        migrations.RemoveField(
            model_name='bannerinfomodel',
            name='product_number',
        ),
        migrations.CreateModel(
            name='ProductSpecificationsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_custom', models.CharField(max_length=99, verbose_name='product_customer')),
                ('product_number', models.CharField(max_length=99, verbose_name='product_numbers')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product', to='home.bannerinfomodel', verbose_name='products')),
            ],
            options={
                'verbose_name': 'product specification',
                'verbose_name_plural': 'product specifications',
            },
        ),
    ]