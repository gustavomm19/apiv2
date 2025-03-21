# Generated by Django 5.1.6 on 2025-03-11 17:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("feedback", "0033_alter_surveytemplate_when_asking_academy_and_more"),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name="surveytemplate",
            unique_together=set(),
        ),
        migrations.AddField(
            model_name="surveytemplate",
            name="original",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="translations",
                to="feedback.surveytemplate",
            ),
        ),
        migrations.AlterUniqueTogether(
            name="surveytemplate",
            unique_together={("original", "lang")},
        ),
    ]
