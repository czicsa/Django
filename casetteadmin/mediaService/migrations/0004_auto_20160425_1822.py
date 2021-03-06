# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-25 16:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mediaService', '0003_media_seq'),
    ]

    operations = [
        migrations.AlterField(
            model_name='media',
            name='media_type',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='media_type', to='typeService.Type'),
        ),
        migrations.AlterField(
            model_name='media',
            name='status_type',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='media_status_type', to='typeService.Type'),
        ),
    ]
