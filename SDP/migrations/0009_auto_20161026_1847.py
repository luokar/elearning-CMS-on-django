# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-26 10:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SDP', '0008_auto_20161026_1829'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enrollment',
            name='completed_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
