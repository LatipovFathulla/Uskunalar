from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_blogmodel_views'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blogmodel',
            options={'ordering': ['-pk'], 'verbose_name': 'blog', 'verbose_name_plural': 'blogs'},
        ),
    ]
