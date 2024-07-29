# Generated by Django 3.2.20 on 2023-08-11 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("provisioning", "0014_auto_20230721_1945"),
    ]

    operations = [
        migrations.AddField(
            model_name="provisioningbill",
            name="archived_at",
            field=models.DateTimeField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name="provisioningbill",
            name="hash",
            field=models.CharField(blank=True, db_index=True, default=None, max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name="provisioningbill",
            name="paid_at",
            field=models.DateTimeField(blank=True, db_index=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name="provisioningbill",
            name="status",
            field=models.CharField(
                choices=[
                    ("DUE", "Due"),
                    ("DISPUTED", "Disputed"),
                    ("IGNORED", "Ignored"),
                    ("PENDING", "Pending"),
                    ("PAID", "Paid"),
                    ("ERROR", "Error"),
                ],
                db_index=True,
                default="DUE",
                max_length=20,
            ),
        ),
    ]
