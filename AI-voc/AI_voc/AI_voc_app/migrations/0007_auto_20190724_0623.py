# Generated by Django 2.2.3 on 2019-07-24 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AI_voc_app', '0006_auto_20190724_0609'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dictionary',
            name='word',
            field=models.CharField(default='', max_length=30),
        ),
    ]
