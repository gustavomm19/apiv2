# Generated by Django 5.0.6 on 2024-05-21 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("provisioning", "0015_auto_20230811_0645"),
    ]

    operations = [
        migrations.AlterField(
            model_name="provisioningconsumptionevent",
            name="repository_url",
            field=models.URLField(null=True),
        ),
        migrations.AlterField(
            model_name="provisioningconsumptionevent",
            name="task_associated_slug",
            field=models.SlugField(
                help_text="What assignment was the the student trying to complete with this", max_length=100, null=True
            ),
        ),
    ]
