# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ttsx_user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='heroinfo',
            name='ubia',
            field=models.CharField(default=b'', max_length=6),
        ),
        migrations.AlterField(
            model_name='heroinfo',
            name='udd',
            field=models.CharField(default=b'', max_length=100),
        ),
        migrations.AlterField(
            model_name='heroinfo',
            name='uphone',
            field=models.CharField(default=b'', max_length=11),
        ),
        migrations.AlterField(
            model_name='heroinfo',
            name='ushou',
            field=models.CharField(default=b'', max_length=10),
        ),
    ]
