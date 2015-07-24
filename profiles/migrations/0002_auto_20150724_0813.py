# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='icq',
            field=models.IntegerField(max_length=300, blank=True, verbose_name='ICQ UIN', null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='jabber',
            field=models.CharField(max_length=300, blank=True, verbose_name='XMPP UID', null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='website',
            field=models.URLField(max_length=300, blank=True, verbose_name='Website', null=True),
        ),
    ]
