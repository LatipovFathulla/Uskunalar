# Generated by Django 4.0 on 2021-12-25 06:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_alter_singlebannermodel_banner_price_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='singlebannermodel',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='home.categorymodel'),
        ),
    ]
