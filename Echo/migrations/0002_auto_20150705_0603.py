# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Echo', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Intent',
            new_name='Intents',
        ),
        migrations.RenameField(
            model_name='intents',
            old_name='option',
            new_name='intent',
        ),
        migrations.RenameField(
            model_name='slot',
            old_name='status',
            new_name='name',
        ),
    ]
