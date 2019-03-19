# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0005_auto_20190319_0535'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='file',
            name='status',
        ),
        migrations.RemoveField(
            model_name='text',
            name='status',
        ),
        migrations.RemoveField(
            model_name='video',
            name='status',
        ),
        migrations.AddField(
            model_name='module',
            name='status',
            field=models.IntegerField(default=1, choices=[(1, b'Basic'), (2, b'Medium'), (3, b'Advanced')]),
        ),
    ]
