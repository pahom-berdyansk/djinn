# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-05-18 09:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_extuser_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='extuser',
            name='birth_date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='extuser',
            name='phone',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='extuser',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='Активный'),
        ),
        migrations.AlterField(
            model_name='extuser',
            name='is_admin',
            field=models.BooleanField(default=False, verbose_name='Администратор'),
        ),
    ]
