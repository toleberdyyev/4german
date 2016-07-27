# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20160723_2110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commentreply',
            name='reply_author',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
