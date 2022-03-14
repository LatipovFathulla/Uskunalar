# Generated by Django 4.0 on 2022-03-12 08:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0064_alter_secondsubcategorymodel_category_and_more'),
        ('orders', '0010_remove_ordermodel_products_ordermodel_products'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ordermodel',
            name='products',
        ),
        migrations.AddField(
            model_name='ordermodel',
            name='products',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='orders', to='home.bannerinfomodel', verbose_name='products'),
        ),
    ]