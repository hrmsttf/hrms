# Generated by Django 3.2.5 on 2021-08-24 07:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_auto_20210824_1147'),
    ]

    operations = [
        migrations.CreateModel(
            name='Leave_Balance',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('balance', models.CharField(blank=True, max_length=30, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('modified_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('is_active', models.PositiveSmallIntegerField(default=1)),
                ('device', models.CharField(blank=True, max_length=20, null=True)),
                ('employee', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='employee_id_balance', to='app.employee')),
                ('leave_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='leave_type_id_balance', to='app.leave_type')),
                ('modified_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='modified_balance', to='app.employee')),
            ],
            options={
                'db_table': 'leave_balance',
            },
        ),
    ]
