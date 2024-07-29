# Generated by Django 3.1.2 on 2020-10-21 00:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Application",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("title", models.CharField(max_length=100)),
                (
                    "status",
                    models.CharField(
                        choices=[("OPERATIONAL", "Operational"), ("MINOR", "Minor"), ("CRITICAL", "Critical")],
                        default="OPERATIONAL",
                        max_length=20,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name="Endpoint",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("url", models.CharField(max_length=255)),
                ("test_pattern", models.CharField(max_length=100)),
                ("frequency_in_minutes", models.FloatField(default=0)),
                ("status_code", models.FloatField(default=0)),
                ("response_text", models.TextField()),
                ("last_check", models.DateTimeField()),
                (
                    "status",
                    models.CharField(
                        choices=[("OPERATIONAL", "Operational"), ("MINOR", "Minor"), ("CRITICAL", "Critical")],
                        default="OPERATIONAL",
                        max_length=20,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
