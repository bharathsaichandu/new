# Generated by Django 2.0.5 on 2019-01-02 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0011_auto_20190102_1857'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shared_room',
            name='otheramenities',
        ),
        migrations.AddField(
            model_name='shared_room',
            name='any_description',
            field=models.TextField(null=True),
        ),
    ]
