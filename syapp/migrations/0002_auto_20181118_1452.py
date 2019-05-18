# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-18 14:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('syapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ips',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(default='', max_length=25)),
                ('t_use', models.CharField(default='', max_length=20)),
            ],
        ),
        migrations.RenameField(
            model_name='ysarticle',
            old_name='content',
            new_name='article',
        ),
        migrations.RemoveField(
            model_name='ysarticle',
            name='time',
        ),
        migrations.AddField(
            model_name='ysarticle',
            name='articletime',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AddField(
            model_name='ysarticle',
            name='category',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AddField(
            model_name='ysarticle',
            name='cover',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='ysarticle',
            name='createtime',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='ysarticle',
            name='key',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AddField(
            model_name='ysarticle',
            name='readtimes',
            field=models.SmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='ysarticle',
            name='reserve',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='ysarticle',
            name='source',
            field=models.SmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='ysarticle',
            name='url',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='ysarticle',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]