# Generated by Django 5.0.3 on 2024-03-31 02:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0014_alter_comment_date_add'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='date_add',
            field=models.DateTimeField(default=datetime.datetime(2024, 3, 31, 4, 12, 52, 926891)),
        ),
    ]
