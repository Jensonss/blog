# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-10-30 12:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0003_nav'),
    ]

    operations = [
        migrations.CreateModel(
            name='Site',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('sign', models.CharField(max_length=200)),
                ('me', models.TextField()),
            ],
        ),
    ]
