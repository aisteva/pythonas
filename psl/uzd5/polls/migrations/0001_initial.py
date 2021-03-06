# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2017-05-09 13:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vertybe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vertybe_nr', models.IntegerField()),
                ('pavadinimas', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Vieta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tikslas', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='vertybe',
            name='vieta',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Vieta'),
        ),
    ]
