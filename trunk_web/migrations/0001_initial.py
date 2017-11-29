# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-29 02:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Station',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(help_text='fire station number', max_length=3)),
                ('name', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Talkgroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('dec_id', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='station',
            name='disp_tg',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='station_disp', to='trunk_web.Talkgroup'),
        ),
        migrations.AddField(
            model_name='station',
            name='tac_tg',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='station_tac', to='trunk_web.Talkgroup'),
        ),
    ]