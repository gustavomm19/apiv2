# Generated by Django 3.2.7 on 2021-10-08 23:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("feedback", "0019_review_reviewplatform"),
    ]

    operations = [
        migrations.AlterField(
            model_name="review",
            name="status",
            field=models.CharField(
                choices=[("PENDING", "Pending"), ("REQUESTED", "Requested"), ("DONE", "Done"), ("IGNORE", "Ignore")],
                default="PENDING",
                help_text="Deleted reviews hav status=Ignore",
                max_length=9,
            ),
        ),
    ]
