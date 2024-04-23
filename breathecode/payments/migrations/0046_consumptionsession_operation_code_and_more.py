# Generated by Django 5.0.4 on 2024-04-22 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0045_plan_service_set_planfinancing_selected_service_set_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='consumptionsession',
            name='operation_code',
            field=models.SlugField(default='default',
                                   help_text='Code that identifies the operation, it could be repeated'),
        ),
        migrations.AddField(
            model_name='service',
            name='session_duration',
            field=models.DurationField(blank=True,
                                       default=None,
                                       help_text='Session duration, used in consumption sessions',
                                       null=True),
        ),
    ]
