# Generated by Django 5.0.1 on 2024-02-03 13:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0001_initial'),
        ('operations', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='operationshistory',
            name='date_time',
        ),
        migrations.AlterField(
            model_name='operation',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='operations', to='category.category'),
        ),
        migrations.AlterField(
            model_name='operationshistory',
            name='operation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='history', to='operations.operation'),
        ),
    ]
