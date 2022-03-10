# Generated by Django 4.0 on 2022-03-10 12:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lines', '0012_alter_linemodel_category_alter_linemodel_category_en_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='linemodel',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='lines', to='lines.linecategorymodel', verbose_name='category'),
        ),
        migrations.AlterField(
            model_name='linemodel',
            name='category_en',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='lines', to='lines.linecategorymodel', verbose_name='category'),
        ),
        migrations.AlterField(
            model_name='linemodel',
            name='category_ru',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='lines', to='lines.linecategorymodel', verbose_name='category'),
        ),
        migrations.AlterField(
            model_name='linemodel',
            name='category_uz',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='lines', to='lines.linecategorymodel', verbose_name='category'),
        ),
    ]
