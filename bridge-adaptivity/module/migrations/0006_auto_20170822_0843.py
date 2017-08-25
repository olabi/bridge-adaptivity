# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-22 08:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bridge_lti', '0008_merge_20170821_0859'),
        ('module', '0005_merge_20170821_0859'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='activity',
            name='source',
        ),
        migrations.AddField(
            model_name='activity',
            name='lti_consumer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='bridge_lti.LtiConsumer'),
        ),
        migrations.AddField(
            model_name='activity',
            name='source_context_id',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='activity',
            name='source_launch_url',
            field=models.URLField(max_length=255, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='activity',
            name='source_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]