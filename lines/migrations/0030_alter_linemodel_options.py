from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lines', '0029_remove_linemodel_category_en_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='linemodel',
            options={'ordering': ['-pk'], 'verbose_name': 'line', 'verbose_name_plural': 'lines'},
        ),
    ]