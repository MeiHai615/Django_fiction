# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-15 14:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arts_app', '0007_remove_artsuser_uphone'),
    ]

    operations = [
        migrations.AddField(
            model_name='artsuser',
            name='uphone',
            field=models.CharField(default=1, max_length=11, verbose_name='手机号'),
            preserve_default=False,
        ),
    ]
