# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0020_remove_comment_sib_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='sib_order',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
