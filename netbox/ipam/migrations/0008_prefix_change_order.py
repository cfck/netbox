# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-15 16:08
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ipam', '0007_prefix_ipaddress_add_tenant'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='prefix',
            options={'ordering': ['vrf', 'family', 'prefix'], 'verbose_name_plural': 'prefixes'},
        ),
    ]
