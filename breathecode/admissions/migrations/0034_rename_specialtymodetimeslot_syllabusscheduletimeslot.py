# Generated by Django 3.2.12 on 2022-03-04 19:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("admissions", "0033_rename_specialtymode_syllabusschedule"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="SpecialtyModeTimeSlot",
            new_name="SyllabusScheduleTimeSlot",
        ),
    ]
