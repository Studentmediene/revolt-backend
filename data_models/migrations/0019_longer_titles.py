# Generated by Django 2.0.2 on 2019-02-03 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data_models', '0018_auto_slug_field'),
    ]

    operations = [
        migrations.AlterField(
            model_name='episode',
            name='title',
            field=models.CharField(max_length=250, verbose_name='Tittel'),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=200, verbose_name='Tittel'),
        ),
    ]
