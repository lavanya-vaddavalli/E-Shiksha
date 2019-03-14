# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('courses', '0002_content_file_text_video'),
    ]

    operations = [
        migrations.CreateModel(
            name='ItemBase',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=250)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('content_type', models.ForeignKey(to='contenttypes.ContentType')),
                ('owner', models.ForeignKey(related_name='itembase_related', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OrderField',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='file',
            name='content_type',
        ),
        migrations.RemoveField(
            model_name='file',
            name='created',
        ),
        migrations.RemoveField(
            model_name='file',
            name='id',
        ),
        migrations.RemoveField(
            model_name='file',
            name='owner',
        ),
        migrations.RemoveField(
            model_name='file',
            name='title',
        ),
        migrations.RemoveField(
            model_name='file',
            name='updated',
        ),
        migrations.RemoveField(
            model_name='text',
            name='content_type',
        ),
        migrations.RemoveField(
            model_name='text',
            name='created',
        ),
        migrations.RemoveField(
            model_name='text',
            name='id',
        ),
        migrations.RemoveField(
            model_name='text',
            name='owner',
        ),
        migrations.RemoveField(
            model_name='text',
            name='title',
        ),
        migrations.RemoveField(
            model_name='text',
            name='updated',
        ),
        migrations.RemoveField(
            model_name='video',
            name='content_type',
        ),
        migrations.RemoveField(
            model_name='video',
            name='created',
        ),
        migrations.RemoveField(
            model_name='video',
            name='id',
        ),
        migrations.RemoveField(
            model_name='video',
            name='owner',
        ),
        migrations.RemoveField(
            model_name='video',
            name='title',
        ),
        migrations.RemoveField(
            model_name='video',
            name='updated',
        ),
        migrations.AddField(
            model_name='file',
            name='itembase_ptr',
            field=models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, default=1, serialize=False, to='courses.ItemBase'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='text',
            name='itembase_ptr',
            field=models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, default=1, serialize=False, to='courses.ItemBase'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='video',
            name='itembase_ptr',
            field=models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, default=1, serialize=False, to='courses.ItemBase'),
            preserve_default=False,
        ),
    ]
