# Generated by Django 3.0.8 on 2020-07-14 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mymusic', '0002_auto_20200714_1432'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='album_Title',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='album',
            name='artist_Name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='album',
            name='released',
            field=models.DateField(blank=True, null=True),
        ),
    ]
