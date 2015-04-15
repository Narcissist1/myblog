# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blogengine', '0002_post_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(default=datetime.datetime(2015, 4, 15, 11, 44, 11, 540880, tzinfo=utc), unique=True, max_length=40),
            preserve_default=False,
        ),
    ]
