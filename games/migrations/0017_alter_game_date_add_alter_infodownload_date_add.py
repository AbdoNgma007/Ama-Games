# Generated by Django 5.0.3 on 2024-03-31 01:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0016_alter_game_date_add_alter_infodownload_date_add'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='date_add',
            field=models.DateTimeField(default=datetime.datetime(2024, 3, 31, 3, 50, 27, 47867)),
        ),
        migrations.AlterField(
            model_name='infodownload',
            name='date_add',
            field=models.DateTimeField(default=datetime.datetime(2024, 3, 31, 3, 50, 27, 47867)),
        ),
    ]
