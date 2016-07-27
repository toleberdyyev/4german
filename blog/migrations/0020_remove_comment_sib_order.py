# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0019_auto_20160726_0622'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='sib_order',
        ),
    ]
