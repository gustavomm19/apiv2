# Generated by Django 5.0.3 on 2024-03-07 07:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("authenticate", "0052_delete_scope_remove_app_agreement_version_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="app",
            name="updated_at",
        ),
    ]
