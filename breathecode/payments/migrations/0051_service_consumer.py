# Generated by Django 5.0.6 on 2024-07-16 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("payments", "0050_planfinancing_conversion_info_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="service",
            name="consumer",
            field=models.CharField(
                choices=[
                    ("ADD_CODE_REVIEW", "Add code review"),
                    ("LIVE_CLASS_JOIN", "Live class join"),
                    ("EVENT_JOIN", "Event join"),
                    ("JOIN_MENTORSHIP", "Join mentorship"),
                    ("READ_LESSON", "Read lesson"),
                    ("NO_SET", "No set"),
                ],
                default="NO_SET",
                help_text="Service type",
                max_length=15,
            ),
        ),
    ]