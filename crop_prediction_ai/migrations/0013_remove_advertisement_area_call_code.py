# Generated by Django 3.2.3 on 2021-08-01 06:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crop_prediction_ai', '0012_auto_20210801_1227'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='advertisement',
            name='area_call_code',
        ),
    ]