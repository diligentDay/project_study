# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AreaInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('atitle', models.CharField(max_length=30)),
                ('aParent', models.ForeignKey(blank=True, to='Areainfo.AreaInfo', null=True)),
            ],
        ),
    ]
