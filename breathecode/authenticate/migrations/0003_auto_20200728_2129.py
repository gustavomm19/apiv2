# Generated by Django 3.0.8 on 2020-07-28 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("authenticate", "0002_credentialsquickbooks"),
    ]

    operations = [
        migrations.AlterField(
            model_name="credentialsgithub",
            name="avatar_url",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name="credentialsgithub",
            name="bio",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name="credentialsgithub",
            name="blog",
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name="credentialsgithub",
            name="company",
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name="credentialsgithub",
            name="name",
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]
