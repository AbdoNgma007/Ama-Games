# Generated by Django 5.0.3 on 2024-03-31 00:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0007_alter_game_date_add_alter_gameimage_game_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='date_add',
            field=models.DateTimeField(default=datetime.datetime(2024, 3, 31, 2, 54, 7, 747946)),
        ),
        migrations.AlterField(
            model_name='infodownload',
            name='date_add',
            field=models.DateTimeField(default=datetime.datetime(2024, 3, 31, 2, 54, 7, 748943)),
        ),
    ]
