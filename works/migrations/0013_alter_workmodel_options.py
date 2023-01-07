from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('works', '0012_alter_workimagemodel_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='workmodel',
            options={'ordering': ['-pk'], 'verbose_name': 'work', 'verbose_name_plural': 'works'},
        ),
    ]
