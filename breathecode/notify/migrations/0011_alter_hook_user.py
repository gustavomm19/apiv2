# Generated by Django 5.0.1 on 2024-01-11 00:51

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("notify", "0010_auto_20220901_0323"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name="hook",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, related_name="%(class)ss", to=settings.AUTH_USER_MODEL
            ),
        ),
    ]
