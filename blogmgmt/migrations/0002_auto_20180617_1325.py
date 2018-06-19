# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blogmgmt', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImageComment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('key', models.CharField(default=uuid.uuid4, max_length=32, editable=False)),
                ('comment_text', models.TextField(max_length=4000)),
                ('commented_on', models.DateTimeField(default=django.utils.timezone.now)),
                ('author', models.ForeignKey(default='', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('post', models.ForeignKey(related_name='comments', to='blogmgmt.Image')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ImageLike',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('key', models.CharField(default=uuid.uuid4, max_length=32, editable=False)),
                ('liked_on', models.DateTimeField(default=django.utils.timezone.now)),
                ('post', models.ForeignKey(related_name='likes', to='blogmgmt.Image')),
                ('user', models.ForeignKey(default='', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='image',
            name='uploaded_on',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=True,
        ),
    ]
