# Generated by Django 2.0.2 on 2018-09-27 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data_models', '0013_settings'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='ready_to_be_published',
            field=models.BooleanField(default=True, help_text='Artikkelen vil aldri bli publisert før denne er huket av. Dette er uavhengig av hvilket publiseringstidspunkt som er satt ovenfor. ', verbose_name='Klar til publisering'),
        ),

        migrations.AlterField(
            model_name='post',
            name='ready_to_be_published',
            field=models.BooleanField(default=False, help_text='Artikkelen vil aldri bli publisert før denne er huket av. Dette er uavhengig av hvilket publiseringstidspunkt som er satt ovenfor. ', verbose_name='Klar til publisering'),
        ),
    ]
