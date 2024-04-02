# Generated by Django 3.1.3 on 2020-11-10 03:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('admissions', '0011_auto_20201006_0058'),
        ('authenticate', '0010_auto_20201105_0531'),
    ]

    operations = [
        migrations.CreateModel(
            name='CredentialsFacebook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(max_length=255)),
                ('expires_at', models.DateTimeField()),
                ('facebook_id', models.BigIntegerField(default=None, null=True)),
                ('email', models.CharField(default=None, max_length=150, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('academy',
                 models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE,
                                      to='admissions.academy')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE,
                                              to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
