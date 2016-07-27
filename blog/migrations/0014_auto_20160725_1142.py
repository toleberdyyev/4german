# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_auto_20160725_1027'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='depth',
            field=models.PositiveIntegerField(default=0, db_index=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='comment',
            name='lft',
            field=models.PositiveIntegerField(default=0, db_index=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='comment',
            name='rgt',
            field=models.PositiveIntegerField(default=0, db_index=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='comment',
            name='tree_id',
            field=models.PositiveIntegerField(default=0, db_index=True),
            preserve_default=False,
        ),
    ]
