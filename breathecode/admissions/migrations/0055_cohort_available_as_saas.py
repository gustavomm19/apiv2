# Generated by Django 3.2.16 on 2023-02-22 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admissions', '0054_cohortuser_history_log'),
    ]

    operations = [
        migrations.AddField(
            model_name='cohort',
            name='available_as_saas',
            field=models.BooleanField(default=False,
                                      help_text='Cohorts available as SAAS will be sold through plans at 4Geeks.com'),
        ),
    ]
