# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0003_remove_blogentry_highlighted'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogentry',
            name='author',
            field=models.ForeignKey(related_name='blog_entry', to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
    ]
