# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-05-19 13:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0002_subscription'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='plans',
            field=models.CharField(choices=[('plan_F5eyGdYCvZPtON', 'Monthly - £24.99'), ('plan_F5ey2nnZwy5v8Q', '3 Months - £49.99'), ('plan_F5eyNlWXHig7YB', '6 Months - £74.99')], default='plan_F5ey2nnZwy5v8Q', max_length=100),
        ),
    ]