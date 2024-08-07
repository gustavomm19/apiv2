# Generated by Django 3.2.15 on 2022-09-20 11:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("admissions", "0045_alter_syllabusversion_integrity_status"),
    ]

    operations = [
        migrations.AlterField(
            model_name="academy",
            name="active_campaign_slug",
            field=models.SlugField(blank=True, default=None, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="academy",
            name="timezone",
            field=models.CharField(blank=True, default=None, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name="cohort",
            name="schedule",
            field=models.ForeignKey(
                blank=True,
                default=None,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="admissions.syllabusschedule",
            ),
        ),
        migrations.AlterField(
            model_name="cohort",
            name="syllabus_version",
            field=models.ForeignKey(
                blank=True,
                default=None,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="admissions.syllabusversion",
            ),
        ),
        migrations.AlterField(
            model_name="cohort",
            name="timezone",
            field=models.CharField(blank=True, default=None, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name="cohortuser",
            name="educational_status",
            field=models.CharField(
                blank=True,
                choices=[
                    ("ACTIVE", "Active"),
                    ("POSTPONED", "Postponed"),
                    ("GRADUATED", "Graduated"),
                    ("SUSPENDED", "Suspended"),
                    ("DROPPED", "Dropped"),
                ],
                default=None,
                max_length=15,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="cohortuser",
            name="finantial_status",
            field=models.CharField(
                blank=True,
                choices=[("FULLY_PAID", "Fully Paid"), ("UP_TO_DATE", "Up to date"), ("LATE", "Late")],
                default=None,
                max_length=15,
                null=True,
            ),
        ),
    ]
