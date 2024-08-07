# Generated by Django 3.2.16 on 2022-10-29 01:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("registry", "0015_auto_20221026_0340"),
    ]

    operations = [
        migrations.AddField(
            model_name="assettechnology",
            name="sort_priority",
            field=models.IntegerField(
                choices=[(1, 1), (2, 2), (3, 3)], default=3, help_text="Priority to sort technology (1, 2, or 3)"
            ),
        ),
    ]
