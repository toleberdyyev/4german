# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_auto_20160724_0841'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='commentreply',
            name='comment',
        ),
        migrations.RemoveField(
            model_name='commentreply',
            name='reply_author',
        ),
        migrations.AddField(
            model_name='comment',
            name='parent',
            field=models.ForeignKey(related_name='replies', to='blog.Comment', null=True),
        ),
        migrations.DeleteModel(
            name='CommentReply',
        ),
    ]
