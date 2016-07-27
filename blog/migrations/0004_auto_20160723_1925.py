# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_commentreply'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commentreply',
            name='author',
            field=models.CharField(max_length=200),
        ),
    ]
