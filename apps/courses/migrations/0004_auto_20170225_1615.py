# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-02-25 16:15
from __future__ import unicode_literals

import DjangoUeditor.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_bannercourse'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='detail',
            field=DjangoUeditor.models.UEditorField(default=b'', verbose_name='\u8bfe\u7a0b\u8be6\u60c5'),
        ),
    ]
