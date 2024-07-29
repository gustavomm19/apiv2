# Generated by Django 3.1.1 on 2020-09-29 18:12

import django.contrib.auth.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
        ("admissions", "0009_academy_logo_url"),
    ]

    operations = [
        migrations.CreateModel(
            name="UserAdmissions",
            fields=[],
            options={
                "proxy": True,
                "indexes": [],
                "constraints": [],
            },
            bases=("auth.user",),
            managers=[
                ("objects", django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.AddField(
            model_name="academy",
            name="website_url",
            field=models.CharField(blank=True, default=None, max_length=255, null=True),
        ),
    ]
