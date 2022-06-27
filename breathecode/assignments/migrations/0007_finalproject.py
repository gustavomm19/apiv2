# Generated by Django 3.2.13 on 2022-06-21 16:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('admissions', '0041_cohortuser_watching'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('assignments', '0006_cohortproxy_userproxy'),
    ]

    operations = [
        migrations.CreateModel(
            name='FinalProject',
            fields=[
                ('id',
                 models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('one_line_desc', models.CharField(max_length=150)),
                ('description', models.TextField()),
                ('project_status',
                 models.CharField(choices=[('PENDING', 'Pending'), ('DONE', 'Done')],
                                  default='PENDING',
                                  help_text='Done projects will be reviewed for publication',
                                  max_length=15)),
                ('revision_status',
                 models.CharField(
                     choices=[('PENDING', 'Pending'), ('APPROVED', 'Approved'), ('REJECTED', 'Rejected')],
                     default='PENDING',
                     help_text='Only approved projects will display on the feature projects list',
                     max_length=15)),
                ('revision_message', models.TextField(blank=True, default=None, null=True)),
                ('visibility_status',
                 models.CharField(choices=[('PRIVATE', 'Private'), ('UNLISTED', 'Unlisted'),
                                           ('PUBLIC', 'Public')],
                                  default='PRIVATE',
                                  help_text='Public project will be visible to other users',
                                  max_length=15)),
                ('repo_url', models.URLField(blank=True, default=None, null=True)),
                ('public_url', models.URLField(blank=True, default=None, null=True)),
                ('logo_url', models.URLField(blank=True, default=None, null=True)),
                ('slides_url', models.URLField(blank=True, default=None, null=True)),
                ('video_demo_url', models.URLField(blank=True, default=None, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('cohort',
                 models.ForeignKey(blank=True,
                                   null=True,
                                   on_delete=django.db.models.deletion.CASCADE,
                                   to='admissions.cohort')),
                ('members', models.ManyToManyField(related_name='final_projects',
                                                   to=settings.AUTH_USER_MODEL)),
                ('repo_owner',
                 models.ForeignKey(blank=True,
                                   null=True,
                                   on_delete=django.db.models.deletion.SET_NULL,
                                   related_name='projects_owned',
                                   to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]