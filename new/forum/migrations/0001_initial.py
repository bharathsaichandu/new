# Generated by Django 2.0.5 on 2018-12-31 18:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import forum.models
import multiselectfield.db.fields
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('taggit', '0002_auto_20150616_2121'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to=forum.models.upload_location, verbose_name='Image(optional)')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='default', upload_to='profile_pics')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('height_field', models.IntegerField(default=0)),
                ('width_field', models.IntegerField(default=0)),
                ('description', models.TextField(null=True)),
                ('user', models.CharField(max_length=120, null=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('tags', taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
            ],
            options={
                'ordering': ['-updated', '-timestamp'],
            },
        ),
        migrations.CreateModel(
            name='share_room_Images',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to=forum.models.upload_location, verbose_name='Image(optional)')),
            ],
        ),
        migrations.CreateModel(
            name='shared_room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=120, null=True)),
                ('email', models.EmailField(max_length=120, null=True)),
                ('City', models.CharField(max_length=100, null=True)),
                ('Area', models.CharField(max_length=100, null=True)),
                ('Address', models.CharField(max_length=200, null=True)),
                ('rent', models.IntegerField()),
                ('securitydeposit', models.IntegerField()),
                ('Area_sqft', models.IntegerField()),
                ('bathrooms', models.IntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)], default=0)),
                ('Furniture', models.CharField(choices=[('full', 'full furnished'), ('semi', 'semi furnished'), ('no', 'no furnished')], max_length=20)),
                ('Available', models.CharField(choices=[('yes', 'Yes'), ('no', 'No')], max_length=10)),
                ('essentialamenities', multiselectfield.db.fields.MultiSelectField(choices=[('parking', 'Car parking'), ('security', 'Security services'), ('water', 'Water supply'), ('elevator', 'Elevators'), ('power', 'Power backup'), ('maintenance', '24-hour maintenance')], default='parking', max_length=49)),
                ('optionalamenities', multiselectfield.db.fields.MultiSelectField(choices=[('play', 'Play area'), ('gym', 'Gym'), ('salon', 'Spa and salon'), ('Concierge', 'Concierge services'), ('hospital', 'Hospitals'), ('restaurant', 'Restaurants'), ('temples', 'Temple and religious activity place'), ('wifi', 'Wi-Fi connectivity')], default='play', max_length=57)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('otheramenities', taggit.managers.TaggableManager(blank=True, help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
            ],
            options={
                'ordering': ['-updated', '-timestamp'],
            },
        ),
        migrations.AddField(
            model_name='share_room_images',
            name='sharedroom',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='forum.shared_room'),
        ),
        migrations.AddField(
            model_name='images',
            name='questionn',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='forum.question'),
        ),
    ]
