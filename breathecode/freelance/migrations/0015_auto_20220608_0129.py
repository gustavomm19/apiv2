# Generated by Django 3.2.13 on 2022-06-08 01:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('admissions', '0041_cohortuser_watching'),
        ('freelance', '0014_alter_bill_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='issue',
            name='academy',
            field=models.ForeignKey(blank=True,
                                    default=None,
                                    help_text='Will help catalog billing grouped by academy',
                                    null=True,
                                    on_delete=django.db.models.deletion.CASCADE,
                                    to='admissions.academy'),
        ),
        migrations.AlterField(
            model_name='bill',
            name='academy',
            field=models.ForeignKey(blank=True,
                                    default=None,
                                    help_text='Will help catalog billing grouped by academy',
                                    null=True,
                                    on_delete=django.db.models.deletion.CASCADE,
                                    to='admissions.academy'),
        ),
    ]
