# Generated by Django 4.2.17 on 2025-01-17 03:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('DSR_APP', '0003_alter_dsr_total_qty_sold'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dsr',
            name='new_total',
        ),
    ]
