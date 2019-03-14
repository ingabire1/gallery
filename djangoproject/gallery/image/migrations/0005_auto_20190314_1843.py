# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-03-14 16:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('image', '0004_auto_20190314_1841'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='category',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='image.Category'),
        ),
        migrations.AlterField(
            model_name='image',
            name='image_image',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='image',
            name='location',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='image.location'),
        ),
    ]
