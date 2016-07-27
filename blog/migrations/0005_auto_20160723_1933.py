# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20160723_1925'),
    ]

    operations = [
        migrations.RenameField(
            model_name='commentreply',
            old_name='author',
            new_name='reply_author',
        ),
    ]
