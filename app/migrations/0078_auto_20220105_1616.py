# Generated by Django 3.2.5 on 2022-01-05 16:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0077_auto_20220105_1614'),
    ]

    operations = [
        migrations.RenameField(
            model_name='attendance',
            old_name='checkin_active',
            new_name='checkin_actived',
        ),
        migrations.RenameField(
            model_name='attendance',
            old_name='checkout_active',
            new_name='checkout_actived',
        ),
    ]