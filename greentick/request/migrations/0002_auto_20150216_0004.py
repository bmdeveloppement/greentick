# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('request', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='file',
            field=models.FileField(null=True, upload_to=b''),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='request',
            name='file',
            field=models.FileField(null=True, upload_to=b''),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='request',
            name='tracking_reference',
            field=models.CharField(max_length=200, null=True),
            preserve_default=True,
        ),
    ]
