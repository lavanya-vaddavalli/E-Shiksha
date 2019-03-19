# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_auto_20150707_1152'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='status',
            field=models.IntegerField(default=1, choices=[(1, b'Basic'), (2, b'Medium'), (3, b'Advanced')]),
        ),
        migrations.AddField(
            model_name='image',
            name='status',
            field=models.IntegerField(default=1, choices=[(1, b'Basic'), (2, b'Medium'), (3, b'Advanced')]),
        ),
        migrations.AddField(
            model_name='text',
            name='status',
            field=models.IntegerField(default=1, choices=[(1, b'Basic'), (2, b'Medium'), (3, b'Advanced')]),
        ),
        migrations.AddField(
            model_name='video',
            name='status',
            field=models.IntegerField(default=1, choices=[(1, b'Basic'), (2, b'Medium'), (3, b'Advanced')]),
        ),
    ]
