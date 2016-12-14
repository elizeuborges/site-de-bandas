# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('bands', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='member',
            options={'ordering': ['name'], 'verbose_name': 'member', 'verbose_name_plural': 'members'},
        ),
        migrations.AddField(
            model_name='member',
            name='band',
            field=models.ForeignKey(related_name='band', default=datetime.datetime(2015, 10, 18, 19, 48, 18, 751000, tzinfo=utc), to='bands.Band'),
            preserve_default=False,
        ),
    ]
