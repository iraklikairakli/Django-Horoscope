# Generated by Django 3.1.2 on 2020-11-02 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_site', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signslist',
            name='Image',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='signslist',
            name='Title',
            field=models.TextField(blank=True),
        ),
    ]
