# Generated by Django 4.0 on 2022-02-14 11:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0029_remove_bannerinfomodel_product_customs_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productspecificationsmodel',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='specification', to='home.bannerinfomodel', verbose_name='products'),
        ),
    ]
