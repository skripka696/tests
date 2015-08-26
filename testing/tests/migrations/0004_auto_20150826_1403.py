# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tests', '0003_auto_20150826_1342'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='status',
            field=models.BooleanField(),
        ),
    ]
