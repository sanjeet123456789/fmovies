# Generated by Django 2.2 on 2019-09-15 06:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies_list', '0016_movies_list_thumbnail'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movies_list',
            old_name='thumbnail',
            new_name='movies_thumbnail',
        ),
    ]
