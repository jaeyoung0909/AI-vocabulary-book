# Generated by Django 2.2.3 on 2019-07-14 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AI_voc_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='vocabulary',
            name='check',
            field=models.IntegerField(default=0),
        ),
    ]
