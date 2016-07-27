# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_auto_20160725_1208'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='depth',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='lft',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='parent',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='rgt',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='tree_id',
        ),
    ]
