# Generated by Django 5.0.3 on 2024-04-06 21:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0021_alter_comment_date_add'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='date_add',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 6, 23, 7, 39, 828740)),
        ),
    ]
