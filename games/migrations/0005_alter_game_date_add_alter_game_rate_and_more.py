# Generated by Django 5.0.3 on 2024-03-30 21:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0004_remove_game_images_alter_game_date_add_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='date_add',
            field=models.DateTimeField(default=datetime.datetime(2024, 3, 30, 23, 10, 42, 104316)),
        ),
        migrations.AlterField(
            model_name='game',
            name='rate',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='infodownload',
            name='date_add',
            field=models.DateTimeField(default=datetime.datetime(2024, 3, 30, 23, 10, 42, 104316)),
        ),
    ]
