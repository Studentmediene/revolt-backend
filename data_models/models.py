from django.db import models
from django.contrib.auth.models import User
from django.utils.crypto import get_random_string
from django.db import IntegrityError
from datetime import datetime
from django.utils.text import slugify


class Show(models.Model):
    name = models.CharField(max_length=64, unique=True)
    slug = models.CharField(max_length=64, unique=True)
    image = models.ImageField(upload_to='uploads/images')
    lead = models.CharField(max_length=140)
    content = models.TextField()

    archived = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT, null=True)

    def save(self, *args, **kwargs):
        if not self.id:
            slug = slugify(self.name, allow_unicode=True)
            try:
                self.slug = slug
            except IntegrityError:
                self.slug = '{slug}-{random_string}'.format(slug=slug, random_string=get_random_string(length=7))

        super(Show, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return str(self.__unicode__())


class Episode(models.Model):
    title = models.CharField(max_length=64)
    lead = models.CharField(max_length=140)

    show = models.ForeignKey(Show, related_name='episodes')

    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT, null=True)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    on_demand_url = models.URLField(help_text="http://hemingway.radiorevolt.no/ondemandinfo/")

    def __unicode__(self):
        return self.title

    def __str__(self):
        return str(self.__unicode__())


class Post(models.Model):
    title = models.CharField(max_length=64)
    slug = models.CharField(max_length=64, unique=True, editable=False)
    image = models.ImageField(upload_to='uploads/images')
    lead = models.CharField(max_length=300)
    content = models.TextField()
    deleted = models.BooleanField(default=False)

    show = models.ForeignKey(Show, blank=True, null=True, related_name='posts')

    publish_at = models.DateTimeField(default=datetime.now)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT, related_name='publications')

    def save(self, *args, **kwargs):
        if not self.id:
            slug = slugify(self.title, allow_unicode=True)
            try:
                self.slug = slug
            except IntegrityError:
                self.slug = '{slug}-{random_string}'.format(slug=slug, random_string=get_random_string(length=7))

        super(Post, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.title

    def __str__(self):
        return str(self.__unicode__())
