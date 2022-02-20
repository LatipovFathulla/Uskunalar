# Generated by Django 4.0.1 on 2022-02-19 11:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0033_alter_subcategorymodel_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='subcategorymodel',
            name='image',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sub_image', to='home.categorymodel', verbose_name='sub_image'),
        ),
    ]