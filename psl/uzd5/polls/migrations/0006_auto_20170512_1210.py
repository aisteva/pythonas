# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2017-05-12 12:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0005_aktas_pavadinimas'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vieta',
            name='vertybe',
        ),
        migrations.AddField(
            model_name='aktas',
            name='vertybe',
            field=models.ManyToManyField(to='polls.Vertybe'),
        ),
    ]
