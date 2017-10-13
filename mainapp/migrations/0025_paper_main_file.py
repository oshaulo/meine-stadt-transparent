# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-07 13:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0024_paper_legal_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='paper',
            name='main_file',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='paper_main_file', to='mainapp.File'),
        ),
    ]