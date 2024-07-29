# Generated by Django 3.2.13 on 2022-08-11 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("assignments", "0008_auto_20220711_1823"),
    ]

    operations = [
        migrations.AddField(
            model_name="task",
            name="subtasks",
            field=models.JSONField(
                blank=True,
                default=None,
                help_text="If readme contains checkboxes they will be converted into substasks and this json will kep track of completition",
                null=True,
            ),
        ),
    ]
