# Generated by Django 5.1.6 on 2025-03-03 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("authenticate", "0068_alter_notfoundanongoogleuser_id_token"),
    ]

    operations = [
        migrations.AddField(
            model_name="userinvite",
            name="expires_at",
            field=models.DateTimeField(blank=True, default=None, null=True),
        ),
    ]
