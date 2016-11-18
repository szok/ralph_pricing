# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-18 09:52
from __future__ import unicode_literals

import datetime
from django.db.models import Count
from django.db import migrations, models


def find_uid_duplicates(apps, schema_editor):
    Service = apps.get_model('ralph_scrooge', 'Service')
    duplicates = Service.objects.values('ci_uid').annotate(
        Count('ci_uid')
    ).order_by().filter(ci_uid__count__gt=1)

    if duplicates:
        raise Exception((
            'Can not run migration, '
            'you have duplicate uid values in Service model.'
            'Duplicates: \n{}'.format(
                ', '.join([i['ci_uid'] for i in duplicates])
            )
        ))


class Migration(migrations.Migration):

    dependencies = [
        ('ralph_scrooge', '0002_auto_20161104_1323'),
    ]

    operations = [
        migrations.RunPython(
            find_uid_duplicates,
            reverse_code=migrations.RunPython.noop
        ),
        migrations.AlterField(
            model_name='historicalservice',
            name='ci_uid',
            field=models.CharField(db_index=True, default=datetime.datetime(2016, 11, 18, 9, 52, 13, 549606), max_length=100, verbose_name='uid from cmdb'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='service',
            name='ci_uid',
            field=models.CharField(default=datetime.datetime(2016, 11, 18, 9, 52, 20, 420682), max_length=100, unique=True, verbose_name='uid from cmdb'),
            preserve_default=False,
        ),
    ]
