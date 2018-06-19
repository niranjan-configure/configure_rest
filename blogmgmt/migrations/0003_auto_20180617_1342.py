# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogmgmt', '0002_auto_20180617_1325'),
    ]

    operations = [
        migrations.RenameField(
            model_name='imagecomment',
            old_name='post',
            new_name='image',
        ),
        migrations.RenameField(
            model_name='imagelike',
            old_name='post',
            new_name='image',
        ),
    ]
