# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-02 02:21
from __future__ import unicode_literals

import django.db.models.deletion
import wagtail.wagtailcore.fields
from django.db import migrations, models

import wagtail_personalisation.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0033_remove_golive_expiry_help_text'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContentPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('subtitle', models.CharField(blank=True, default='', max_length=255)),
                ('body', wagtail.wagtailcore.fields.RichTextField(blank=True, default='')),
            ],
            options={
                'abstract': False,
            },
            bases=(wagtail_personalisation.models.PersonalisablePageMixin, 'wagtailcore.page'),
        ),
    ]