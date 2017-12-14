# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-11-01 16:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('netop', '0004_auto_20171101_0950'),
    ]

    operations = [
        migrations.AddField(
            model_name='configurationrequisition',
            name='signer',
            field=models.CharField(choices=[('1', '胡云'), ('2', '刘志伟'), ('3', '杨杉'), ('4', '杜振华'), ('5', '韩玉')], default=1, max_length=6, verbose_name='确认人员'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='configurationrequisition',
            name='change_operation_confirmation',
            field=models.CharField(choices=[('1', '已确认'), ('2', '待完善')], max_length=6, verbose_name='操作确认'),
        ),
        migrations.AlterField(
            model_name='configurationrequisition',
            name='change_preparation_confirmation',
            field=models.CharField(choices=[('1', '已确认'), ('2', '待完善')], max_length=6, verbose_name='准备确认'),
        ),
        migrations.AlterField(
            model_name='configurationrequisition',
            name='change_process_validation',
            field=models.CharField(choices=[('1', '已确认'), ('2', '待完善')], max_length=6, verbose_name='流程确认'),
        ),
    ]
