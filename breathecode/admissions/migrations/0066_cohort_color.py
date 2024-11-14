# Generated by Django 5.1.2 on 2024-11-14 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("admissions", "0065_cohort_cohorts_order_cohort_micro_cohorts"),
    ]

    operations = [
        migrations.AddField(
            model_name="cohort",
            name="color",
            field=models.CharField(
                blank=True,
                default=None,
                help_text="Add the color with hexadecimal format, i.e.: #FFFFFF",
                max_length=50,
                null=True,
            ),
        ),
    ]
