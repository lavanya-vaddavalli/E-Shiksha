# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0004_auto_20190319_0533'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='owner',
        ),
        migrations.DeleteModel(
            name='Image',
        ),
    ]
