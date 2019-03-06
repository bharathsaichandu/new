# Generated by Django 2.0.5 on 2019-01-02 13:27

from django.db import migrations
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0009_shared_room_beds_available'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shared_room',
            name='otheramenities',
            field=taggit.managers.TaggableManager(blank=True, help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
    ]