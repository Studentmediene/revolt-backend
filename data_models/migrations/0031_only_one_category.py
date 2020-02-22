'''
1. Legg til den nederste linjen i show modellen under data_models.models
2. Legg til denne filen som en migration og kjør migrate
3. fjern linjen med categories i show modellen
4. runserver og gå i adminpanelet for å sjekke


Må gjøres:
* oppdatere frontend queries
* oppdatere graphql queries på backend
'''

import django.db.models.deletion
from django.db import models, migrations

def forward(apps, schema_editor):
    Shows = apps.get_model("data_models","Show")
    for show in Shows.objects.all():
        for cat in show.categories.all():
            show.category = cat
            show.save()
        

class Migration(migrations.Migration):

    dependencies = [
        ('data_models', '0030_add_producers'),
    ]

    operations = [
        migrations.AddField(
            model_name='show',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='enkelt_kategori', to='data_models.Category', verbose_name='Kategori'),
        ),
        migrations.RunPython(forward),
        migrations.RemoveField(
            model_name='show',
            name='categories',
        ),
    ]

# category = models.ForeignKey(Category, models.SET_NULL, null=True, blank=True, verbose_name='Kategori', related_name='enkelt_kategori')