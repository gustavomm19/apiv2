# Generated by Django 3.2.16 on 2022-11-09 02:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("registry", "0018_auto_20221101_0235"),
    ]

    operations = [
        migrations.AddField(
            model_name="asset",
            name="is_seo_tracked",
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name="seoreport",
            name="how_to_fix",
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name="seoreport",
            name="log",
            field=models.JSONField(blank=True, default=None, null=True),
        ),
    ]
