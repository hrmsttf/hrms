# Generated by Django 3.2.5 on 2021-12-29 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0068_timelogs_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='timelogs',
            name='decription',
            field=models.TextField(blank=True, null=True),
        ),
    ]
