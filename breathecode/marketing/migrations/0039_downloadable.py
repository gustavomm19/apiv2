# Generated by Django 3.2.7 on 2021-10-09 01:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("admissions", "0024_academy_feedback_email"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("marketing", "0038_auto_20210703_0359"),
    ]

    operations = [
        migrations.CreateModel(
            name="Downloadable",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("slug", models.SlugField(max_length=150, unique=True)),
                ("name", models.CharField(max_length=100)),
                ("description", models.TextField(max_length=450)),
                ("hits", models.IntegerField(default=0)),
                (
                    "active",
                    models.BooleanField(
                        default=True, help_text="Non-active downloadables will display a message to the user"
                    ),
                ),
                ("preview_url", models.URLField()),
                ("destination_url", models.URLField()),
                (
                    "destination_status",
                    models.CharField(
                        choices=[("ACTIVE", "Active"), ("NOT_FOUND", "Not found")], default="ACTIVE", max_length=15
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("academy", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="admissions.academy")),
                ("author", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
