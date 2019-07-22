# Generated by Django 2.2.3 on 2019-07-14 21:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('AI_voc_app', '0002_vocabulary_check'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ability',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ability', models.IntegerField(default=0)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='vocabulary',
            name='check',
        ),
        migrations.DeleteModel(
            name='UserAbility',
        ),
        migrations.AddField(
            model_name='ability',
            name='word',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AI_voc_app.Vocabulary'),
        ),
    ]