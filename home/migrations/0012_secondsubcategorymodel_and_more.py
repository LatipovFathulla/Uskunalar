# Generated by Django 4.0 on 2021-12-24 11:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_subcategorymodel_bannerinfomodel_subcategory'),
    ]

    operations = [
        migrations.CreateModel(
            name='SecondSubCategoryModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('secondsubcategory', models.CharField(max_length=90, verbose_name='second_subcategory')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='crated_at')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='home.categorymodel', verbose_name='category')),
                ('subcategory', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='home.subcategorymodel', verbose_name='subcategory')),
            ],
            options={
                'verbose_name': 'subcategory',
                'verbose_name_plural': 'subcategories',
            },
        ),
        migrations.AddField(
            model_name='bannerinfomodel',
            name='secondsubcategory',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='home.secondsubcategorymodel', verbose_name='second_subcategory'),
        ),
    ]
