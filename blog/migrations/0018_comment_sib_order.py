# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0017_comment_parent'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='sib_order',
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
    ]
