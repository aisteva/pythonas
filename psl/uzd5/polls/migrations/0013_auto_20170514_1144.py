# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-14 11:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0012_auto_20170514_1143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='narys',
            name='pareigos',
            field=models.CharField(choices=[('pirmininkas', 'Komisijos pirmininkas'), ('narys', 'Narys')], max_length=200),
        ),
    ]
