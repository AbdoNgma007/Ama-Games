# Generated by Django 5.0.3 on 2024-04-06 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_rename_picture_userprofile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='nationality',
            field=models.CharField(max_length=35),
        ),
    ]
