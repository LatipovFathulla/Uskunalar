# Generated by Django 4.0 on 2022-03-25 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0065_alter_bannerimagemodel_product_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bannerinfomodel',
            name='sku',
            field=models.CharField(db_index=True, max_length=99, primary_key=True, serialize=False),
        ),
    ]