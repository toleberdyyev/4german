# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20160723_1940'),
    ]

    operations = [
        migrations.AddField(
            model_name='commentreply',
            name='approved_comment',
            field=models.BooleanField(default=False),
        ),
    ]
