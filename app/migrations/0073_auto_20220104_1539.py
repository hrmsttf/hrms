# Generated by Django 3.2.5 on 2022-01-04 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0072_auto_20220104_1537'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='employee_id',
            field=models.CharField(max_length=35, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='employee',
            name='other_email',
            field=models.CharField(blank=True, max_length=35, null=True),
        ),
    ]