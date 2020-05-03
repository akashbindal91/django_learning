# Generated by Django 2.2.6 on 2020-03-22 10:26

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 22, 10, 26, 13, 963656, tzinfo=utc)),
        ),
        migrations.AddField(
            model_name='post',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 22, 10, 26, 13, 962656, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='comment',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 22, 10, 26, 13, 963656, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 22, 10, 26, 13, 962656, tzinfo=utc)),
        ),
    ]
