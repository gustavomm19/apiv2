# Generated by Django 5.0.3 on 2024-03-07 07:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("authenticate", "0048_auto_20231128_1224"),
    ]

    operations = [
        migrations.DeleteModel(
            name="AppUserAgreement",
        ),
    ]
