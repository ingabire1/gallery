# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-03-14 16:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('image', '0003_editor_phone_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60)),
            ],
        ),
        migrations.RenameField(
            model_name='image',
            old_name='post',
            new_name='description',
        ),
        migrations.AddField(
            model_name='image',
            name='image_image',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='images/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='image',
            name='category',
            field=models.ForeignKey(default=django.utils.timezone.now, on_delete=django.db.models.deletion.CASCADE, to='image.Category'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='image',
            name='location',
            field=models.ForeignKey(default=django.utils.timezone.now, on_delete=django.db.models.deletion.CASCADE, to='image.location'),
            preserve_default=False,
        ),
    ]