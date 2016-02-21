# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-21 12:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('alter_pk', '0006_author_change_pk'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='author_name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='alter_pk.Author'),
        ),
    ]
