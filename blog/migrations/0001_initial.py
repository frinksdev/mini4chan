# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='chan',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('titulo', models.CharField(max_length=200)),
                ('contenido', models.TextField()),
                ('c_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('p_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('autor', models.ForeignKey(null=True, blank=True, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='comentario',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('comentario', models.TextField()),
                ('p_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('post', models.ForeignKey(to='blog.chan')),
            ],
        ),
    ]
