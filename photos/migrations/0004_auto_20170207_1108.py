# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-07 02:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0003_auto_20170206_0936'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='filtered_image',
            field=models.ImageField(upload_to='%Y/%m/%d/filtered'),
        ),
        migrations.AlterField(
            model_name='photo',
            name='image',
            field=models.ImageField(upload_to='%Y/%m/%d/orig'),
        ),
    ]