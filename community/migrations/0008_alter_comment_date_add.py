# Generated by Django 5.0.3 on 2024-03-31 01:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0007_alter_comment_date_add'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='date_add',
            field=models.DateTimeField(default=datetime.datetime(2024, 3, 31, 3, 47, 58, 702111)),
        ),
    ]
