# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('key', models.CharField(default=uuid.uuid4, max_length=32, editable=False)),
                ('comment_text', models.TextField(max_length=4000)),
                ('commented_on', models.DateTimeField(default=django.utils.timezone.now)),
                ('author', models.ForeignKey(default='', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('key', models.CharField(default=uuid.uuid4, max_length=32, editable=False)),
                ('location', models.CharField(max_length=500)),
                ('description', models.CharField(max_length=500)),
                ('name', models.CharField(max_length=100)),
                ('owner', models.ForeignKey(default='', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('key', models.CharField(default=uuid.uuid4, max_length=32, editable=False)),
                ('liked_on', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('key', models.CharField(default=uuid.uuid4, max_length=32, editable=False)),
                ('message', models.TextField(max_length=4000)),
                ('title', models.CharField(max_length=100)),
                ('posted_on', models.DateTimeField(default=django.utils.timezone.now)),
                ('author', models.ForeignKey(default='', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='like',
            name='post',
            field=models.ForeignKey(related_name='likes', to='blogmgmt.Post'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='like',
            name='user',
            field=models.ForeignKey(default='', blank=True, to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(related_name='comments', to='blogmgmt.Post'),
            preserve_default=True,
        ),
    ]
