# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-08 21:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arts_app', '0005_chapter'),
    ]

    operations = [
        migrations.AddField(
            model_name='artsuser',
            name='uphone',
            field=models.CharField(max_length=11, null=True),
        ),
    ]
