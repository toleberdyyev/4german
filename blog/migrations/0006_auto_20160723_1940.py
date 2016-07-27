# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20160723_1933'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commentreply',
            name='reply_author',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
