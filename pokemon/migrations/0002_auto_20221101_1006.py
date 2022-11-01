# Generated by Django 3.2.16 on 2022-11-01 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pokemon',
            name='description',
        ),
        migrations.AddField(
            model_name='pokemon',
            name='moves',
            field=models.CharField(default='trtr', max_length=256),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pokemon',
            name='weight',
            field=models.PositiveSmallIntegerField(default=2),
            preserve_default=False,
        ),
    ]