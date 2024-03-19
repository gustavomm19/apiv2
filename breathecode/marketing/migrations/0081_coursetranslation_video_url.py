# Generated by Django 5.0.3 on 2024-03-12 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketing', '0080_course_plan_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='coursetranslation',
            name='video_url',
            field=models.URLField(default=None,
                                  help_text='Video that introduces/promotes this course',
                                  null=True),
        ),
    ]