# Generated by Django 3.2.19 on 2023-05-18 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("marketing", "0068_auto_20230429_0045"),
    ]

    operations = [
        migrations.AlterField(
            model_name="activecampaignwebhook",
            name="run_at",
            field=models.DateTimeField(blank=True, default=None, help_text="Date/time that the webhook ran", null=True),
        ),
    ]
