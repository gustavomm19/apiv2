# Generated by Django 3.2.16 on 2022-11-09 22:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketing', '0059_auto_20221004_1943'),
    ]

    operations = [
        migrations.AddField(
            model_name='formentry',
            name='custom_fields',
            field=models.JSONField(
                blank=True,
                default=None,
                help_text='Other incoming values in the payload will be saved here as they come',
                null=True),
        ),
        migrations.AddField(
            model_name='formentry',
            name='sex',
            field=models.CharField(blank=True,
                                   default=None,
                                   help_text='M=male,F=female,O=other',
                                   max_length=15,
                                   null=True),
        ),
        migrations.AddField(
            model_name='formentry',
            name='utm_placement',
            field=models.CharField(blank=True,
                                   default=None,
                                   help_text='User agent or device screen',
                                   max_length=50,
                                   null=True),
        ),
        migrations.AddField(
            model_name='formentry',
            name='utm_plan',
            field=models.CharField(
                blank=True,
                default=None,
                help_text='If its applying for a scholarship, upfront, isa, financing, etc.',
                max_length=50,
                null=True),
        ),
        migrations.AddField(
            model_name='formentry',
            name='utm_term',
            field=models.CharField(blank=True,
                                   default=None,
                                   help_text='Keyword used in cpc',
                                   max_length=50,
                                   null=True),
        ),
        migrations.AddField(
            model_name='leadgenerationapp',
            name='utm_plan',
            field=models.CharField(
                blank=True,
                default=None,
                help_text='If its applying for a scholarship, upfront, isa, financing, etc.',
                max_length=50,
                null=True),
        ),
        migrations.AddField(
            model_name='shortlink',
            name='utm_placement',
            field=models.CharField(blank=True,
                                   default=None,
                                   help_text='User agent or device screen',
                                   max_length=50,
                                   null=True),
        ),
        migrations.AddField(
            model_name='shortlink',
            name='utm_plan',
            field=models.CharField(
                blank=True,
                default=None,
                help_text='If its applying for a scholarship, upfront, isa, financing, etc.',
                max_length=50,
                null=True),
        ),
        migrations.AddField(
            model_name='shortlink',
            name='utm_term',
            field=models.CharField(blank=True,
                                   default=None,
                                   help_text='Keyword used in cpc',
                                   max_length=50,
                                   null=True),
        ),
        migrations.AlterField(
            model_name='shortlink',
            name='utm_campaign',
            field=models.CharField(
                blank=True,
                default=None,
                help_text='Campaign ID when PPC but can be a string in more informal campaigns',
                max_length=50,
                null=True),
        ),
        migrations.AlterField(
            model_name='shortlink',
            name='utm_content',
            field=models.CharField(blank=True,
                                   default=None,
                                   help_text='Can be de ad group id or ad id',
                                   max_length=250,
                                   null=True),
        ),
        migrations.AlterField(
            model_name='shortlink',
            name='utm_medium',
            field=models.CharField(blank=True,
                                   default=None,
                                   help_text='social, organic, paid, email, referral, etc.',
                                   max_length=50,
                                   null=True),
        ),
        migrations.AlterField(
            model_name='shortlink',
            name='utm_source',
            field=models.CharField(blank=True,
                                   default=None,
                                   help_text='fb, ig, google, twitter, quora, etc.',
                                   max_length=50,
                                   null=True),
        ),
    ]
