# Generated by Django 2.0.2 on 2018-10-04 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data_models', '0016_privacy_policy_in_settings'),
    ]

    operations = [
        migrations.AlterField(
            model_name='show',
            name='slug',
            field=models.CharField(editable=False, max_length=64, unique=True),
        ),
    ]
