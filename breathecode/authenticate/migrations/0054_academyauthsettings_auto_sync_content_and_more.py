# Generated by Django 5.0.3 on 2024-03-28 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authenticate', '0053_remove_app_updated_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='academyauthsettings',
            name='auto_sync_content',
            field=models.BooleanField(
                default=False, help_text='If true, will attempt to create WebhookSubscription on each asset repo'),
        ),
        migrations.AlterField(
            model_name='academyauthsettings',
            name='github_is_sync',
            field=models.BooleanField(default=False, help_text='If true, will try synching users every few hours'),
        ),
    ]
