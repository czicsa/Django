# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-24 13:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('typeService', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('media_title', models.CharField(max_length=200)),
                ('purchase_date', models.DateField()),
                ('media_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='media_type', to='typeService.Type')),
                ('status_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='media_status_type', to='typeService.Type')),
            ],
        ),
    ]
