# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HeroInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('uname', models.CharField(max_length=20)),
                ('upwd', models.CharField(max_length=40)),
                ('umail', models.CharField(max_length=20)),
                ('ushou', models.CharField(max_length=20)),
                ('udd', models.CharField(max_length=100)),
                ('ubia', models.CharField(max_length=6)),
                ('uphone', models.CharField(max_length=11)),
            ],
        ),
    ]
