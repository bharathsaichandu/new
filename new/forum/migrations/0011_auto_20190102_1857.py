# Generated by Django 2.0.5 on 2019-01-02 13:27

from django.db import migrations
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0010_auto_20190102_1857'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='tags',
            field=taggit.managers.TaggableManager(blank=True, help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
    ]
