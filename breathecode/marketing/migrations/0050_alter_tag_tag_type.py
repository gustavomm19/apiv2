# Generated by Django 3.2.9 on 2022-01-28 03:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketing', '0049_auto_20220127_1806'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='tag_type',
            field=models.CharField(
                choices=[('STRONG', 'Strong'), ('SOFT', 'Soft'), ('DISCOVERY', 'Discovery'), ('COHORT', 'Cohort'),
                         ('DOWNLOADABLE', 'Downloadable'), ('EVENT', 'Event'), ('OTHER', 'Other')],
                default='OTHER',
                help_text=
                "The STRONG tags in a lead will determine to witch automation it does unless there is an 'automation' property on the lead JSON",
                max_length=15,
                null=True),
        ),
    ]
