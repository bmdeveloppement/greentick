# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import request.extras


class Migration(migrations.Migration):

    dependencies = [
        ('request', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='size',
            field=models.IntegerField(default=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='file',
            name='type',
            field=models.IntegerField(default=None),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='file',
            name='file',
            field=request.extras.ContentTypeRestrictedFileField(upload_to='request_attachments/2015/03/01'),
            preserve_default=True,
        ),
    ]
