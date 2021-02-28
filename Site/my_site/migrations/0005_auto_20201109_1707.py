# Generated by Django 3.1.2 on 2020-11-09 17:07

from django.db import migrations, models
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0003_taggeditem_add_unique_index'),
        ('my_site', '0004_auto_20201106_0946'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogmodel',
            name='tags',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
        migrations.AlterField(
            model_name='blogmodel',
            name='slug',
            field=models.SlugField(),
        ),
    ]
