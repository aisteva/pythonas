# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2017-05-12 11:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_auto_20170511_1820'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aktas',
            name='narys',
        ),
        migrations.RemoveField(
            model_name='aktas',
            name='pirkimo_dokumentas',
        ),
        migrations.AddField(
            model_name='aktas',
            name='nariai',
            field=models.ManyToManyField(to='polls.Narys'),
        ),
        migrations.AddField(
            model_name='aktas',
            name='pirkimo_dokumentai',
            field=models.ManyToManyField(to='polls.Pirkimo_Dokumentas'),
        ),
    ]
