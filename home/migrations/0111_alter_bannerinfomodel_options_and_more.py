# Generated by Django 4.0 on 2022-07-30 10:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0110_alter_bannerinfomodel_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bannerinfomodel',
            options={'ordering': ['my_product'], 'verbose_name': 'products', 'verbose_name_plural': 'products'},
        ),
        migrations.RenameField(
            model_name='bannerinfomodel',
            old_name='my_order',
            new_name='my_product',
        ),
    ]