# Generated by Django 3.2.20 on 2023-08-10 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("events", "0050_auto_20230721_0158"),
    ]

    operations = [
        migrations.AlterField(
            model_name="event",
            name="free_for_bootcamps",
            field=models.BooleanField(
                blank=True,
                default=True,
                help_text="Determines if users that belong to an academy not available as saas can join the event for free.",
                null=True,
            ),
        ),
    ]
