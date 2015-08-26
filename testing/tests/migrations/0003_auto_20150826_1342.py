# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tests', '0002_auto_20150826_1333'),
    ]

    operations = [
        migrations.RenameField(
            model_name='statustest',
            old_name='answer',
            new_name='status_answer',
        ),
        migrations.RenameField(
            model_name='statustest',
            old_name='question',
            new_name='status_question',
        ),
    ]
