from datetime import datetime

from colorfield.fields import ColorField
from django.contrib.auth.models import User
from django.db import models
from django_extensions.db.fields import AutoSlugField
from solo.models import SingletonModel
from sorl_cropping import ImageRatioField


class Category(models.Model):
    class Meta:
        verbose_name = "Kategori"
        verbose_name_plural = "Kategorier"

    name = models.CharField('Navn', max_length=64, unique=True)
    text_color = ColorField('Tekstfarge', default='000000')
    background_color = ColorField('Bakgrunnsfarge', default='ECB61C')

    def __unicode__(self):
        return self.name

    def __str__(self):
        return str(self.__unicode__())


class Settings(SingletonModel):
    class Meta:
        verbose_name = 'Innstillinger'

    chief_editor = models.CharField('Ansvarlig redaktør', default="", max_length=128)
    radio_editor = models.CharField('Radioredaktør', default="", max_length=128)
    music_producer = models.CharField('Musikkprodusent', default="", max_length=128)

    about = models.TextField('Om Radio Revolt')

    privacy_policy = models.TextField('Personvernerklæring', default="")

    def __unicode__(self):
        return 'Innstillinger for Radio Revolt'

    def __str__(self):
        return str(self.__unicode__())


class Show(models.Model):
    class Meta:
        verbose_name = "Program"
        verbose_name_plural = "Programmer"

    name = models.CharField('Navn', max_length=64, unique=True)
    slug = AutoSlugField(populate_from=['name'])
    image = models.ImageField('Programlogo', upload_to='uploads/images')
    lead = models.TextField('Kort beskrivelse', max_length=255)
    content = models.TextField('Lang beskrivelse')

    categories = models.ManyToManyField(Category, blank=True, verbose_name='Kategorier')

    archived = models.BooleanField('Arkivert', default=False)

    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)
    created_by = models.ForeignKey(
        User, on_delete=models.PROTECT, null=True, verbose_name='Opprettet av')

    def __unicode__(self):
        return self.name

    def __str__(self):
        return str(self.__unicode__())

    def get_absolute_url(self):
        return '/programmer/' + self.slug


class Episode(models.Model):
    class Meta:
        verbose_name = "Episode"
        verbose_name_plural = "Episoder"
        ordering = ['-created_at']

    title = models.CharField('Tittel', max_length=250)
    use_title = models.BooleanField(
        'Bruk tittel',
        default=False,
        help_text='Vis tittelen på episoden. ' +
        'Om ikke tittel benyttes vises "Navn på show" + "Publiseringsdato"')
    lead = models.TextField('Beskrivelse')

    show = models.ForeignKey(
        Show,
        related_name='episodes',
        verbose_name='Program',
        on_delete=models.CASCADE,
    )

    categories = models.ManyToManyField(Category, blank=True, verbose_name='Kategorier')

    publish_at = models.DateTimeField(default=datetime.now)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    created_by = models.ForeignKey(
        User, on_delete=models.PROTECT, null=True, verbose_name='Opprettet av')
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    on_demand_url = models.URLField(help_text="https://ondemandinfo.radiorevolt.no/")

    def __unicode__(self):
        return self.title

    def __str__(self):
        return str(self.__unicode__())

    def get_absolute_url(self):
        return '/programmer/' + self.show.slug


class Post(models.Model):
    class Meta:
        verbose_name = "Artikkel"
        verbose_name_plural = "Artikler"
        ordering = ['-publish_at']

    title = models.CharField('Tittel', max_length=200)
    slug = AutoSlugField(populate_from=['title'])
    image = models.ImageField('Bilde', upload_to='uploads/images')
    cropping = ImageRatioField(
        'image',
        '1024x512',
        size_warning=True,
        verbose_name='Bildeutsnitt',
        help_text='Velg bildeutsnitt')
    lead = models.CharField('Ingress', max_length=140)
    content = models.TextField('Brødtekst')
    deleted = models.BooleanField('Slettet', default=False)

    episodes = models.ManyToManyField(
        Episode,
        blank=True,
        verbose_name='Episoder',
        help_text='Legger til episoder i bunnen av artikkelen. ' +
        'Episodelisten blir filtrert på valgt program etter at artikkelen er opprettet.')

    show = models.ForeignKey(
        Show,
        blank=True,
        null=True,
        related_name='posts',
        verbose_name='Program',
        on_delete=models.CASCADE)

    categories = models.ManyToManyField(Category, blank=True, verbose_name='Kategorier')

    publish_at = models.DateTimeField('Publisert', default=datetime.now)

    ready_to_be_published = models.BooleanField(
        'Klar til publisering',
        default=False,
        help_text='Artikkelen vil aldri bli publisert før denne er huket av. ' +
        'Dette er uavhengig av hvilket publiseringstidspunkt som er satt ovenfor. ')

    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)
    created_by = models.ForeignKey(
        User, on_delete=models.PROTECT, related_name='publications', verbose_name='Opprettet av')

    def __unicode__(self):
        return self.title

    def __str__(self):
        return str(self.__unicode__())

    def get_absolute_url(self):
        return '/post/' + self.slug


class HighlightedPost(SingletonModel):
    class Meta:
        verbose_name = 'Fremhevede artikler'

    posts = models.ManyToManyField(
        Post,
        blank=True,
        verbose_name='Artikler',
        limit_choices_to={'ready_to_be_published': True},
        help_text='Legg til artikler som skal fremheves på forsiden. Maksimalt 5 artikler.<br>' +
        'Dukker ikke artikkelen opp? Har du husket å markere den som "Klar til publisering"?<br>')

    def __unicode__(self):
        return 'Fremhevede artikler'

    def __str__(self):
        return str(self.__unicode__())
