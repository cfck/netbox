# Generated by Django 2.2 on 2019-04-20 00:57

from django.db import migrations
import django.db.models.expressions


class Migration(migrations.Migration):

    dependencies = [
        ('ipam', '0025_custom_tag_models'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='prefix',
            options={'ordering': [django.db.models.expressions.OrderBy(django.db.models.expressions.F('vrf'), nulls_first=True), 'family', 'prefix'], 'verbose_name_plural': 'prefixes'},
        ),
    ]
