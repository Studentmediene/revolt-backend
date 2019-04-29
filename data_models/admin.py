from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms
from django.contrib import admin
from solo.admin import SingletonModelAdmin
from sorl_cropping import ImageCroppingMixin

from . import rr_api
from .models import Category, Episode, HighlightedPost, Post, Settings, Show


class ShowFilter(admin.SimpleListFilter):
    def lookups(self, request, model_admin):
        shows = Show.objects.filter(archived=self.archived)
        return [(show.id, str(show)) for show in shows]

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(show=self.value())
        else:
            return queryset


class ActiveShowFilter(ShowFilter):
    title = 'aktive programmer'
    parameter_name = 'show'
    archived = False


class ArchivedShowFilter(ShowFilter):
    title = 'arkiverte programmer'
    parameter_name = 'show'
    archived = True


class PostAdminForm(forms.ModelForm):
    content = forms.CharField(
        widget=CKEditorUploadingWidget(),
        label='Brødtekst',
        help_text='Legge til Spotify-spilleliste? Sjekk ut guiden ' +
        '<a href="https://confluence.smint.no/pages/viewpage.action?pageId=36111759"' +
        'target="_blank">her</a>.')

    class Meta:
        model = Post
        fields = '__all__'


class SettingsAdminForm(forms.ModelForm):
    about = forms.CharField(widget=CKEditorUploadingWidget(), label='Om Radio Revolt')
    privacy_policy = forms.CharField(widget=CKEditorUploadingWidget(), label='Personvernerklæring')

    class Meta:
        model = Settings
        fields = '__all__'


def get_show_options():
    shows = rr_api.get_shows()

    def process_shows(predicate):
        filtered_shows = filter(predicate, shows)
        as_choices = map(lambda s: (s['id'], s['name']), filtered_shows)
        return tuple(as_choices)

    # Filter into archived and active
    old_shows = process_shows(lambda s: s['old'])
    active_shows = process_shows(lambda s: not s['old'])

    return (
        (None, '--------'),
        ('Aktive programmer', active_shows),
        ('Arkivert', old_shows),
    )


class ShowAdminForm(forms.ModelForm):
    content = forms.CharField(
        widget=CKEditorUploadingWidget(config_name='small'), label='Lang beskrivelse')

    digas_id = forms.TypedChoiceField(
        coerce=int,
        empty_value=None,
        required=False,
        label='Tilhørende Digas-program',
        choices=get_show_options,
    )

    class Meta:
        model = Show
        fields = '__all__'


class EpisodeAdminForm(forms.ModelForm):
    # lead = forms.CharField(
    #   widget=CKEditorUploadingWidget(config_name='small'), label='Beskrivelse')

    class Meta:
        model = Episode
        fields = '__all__'


class HighlightedPostAdminForm(forms.ModelForm):
    def clean_posts(self):
        posts = self.cleaned_data['posts']
        if len(posts) > 5:
            raise forms.ValidationError("Du kan ikke fremheve mer enn 5 artikler.")
        return posts

    class Meta:
        model = HighlightedPost
        fields = '__all__'


@admin.register(Post)
class PostAdmin(ImageCroppingMixin, admin.ModelAdmin):
    list_display = ('title', 'show', 'publish_at', 'ready_to_be_published', 'deleted')
    list_filter = ('deleted', 'publish_at', 'show')
    search_fields = ('title', 'show__name')
    form = PostAdminForm

    def get_form(self, request, obj, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        if obj and obj.show:
            show_episodes = Episode.objects.filter(show=obj.show)
            form.base_fields['episodes'].queryset = show_episodes
        return form

    # Set form field for "lead" to Textarea instead of Textinput
    def formfield_for_dbfield(self, db_field, **kwargs):
        formfield = super(PostAdmin, self).formfield_for_dbfield(db_field, **kwargs)
        if db_field.name == 'lead':
            formfield.widget = forms.Textarea(attrs={'cols': 60, 'rows': 5})
        return formfield


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Settings)
class SettingsAdmin(SingletonModelAdmin):
    form = SettingsAdminForm


@admin.register(Show)
class ShowAdmin(admin.ModelAdmin):
    list_display = ('name', 'archived', 'is_podcast')
    list_filter = ('archived', 'is_podcast')
    ordering = ('archived', 'name')
    search_fields = ('name', )
    form = ShowAdminForm
    actions = ('make_podcast', 'unmake_podcast')

    def make_podcast(self, request, queryset):
        rows_updated = queryset.update(is_podcast=True)
        self.message_user(request, '{} program(mer) ble markert som podkast'.format(rows_updated))

    make_podcast.short_description = 'Marker som podkast'

    def unmake_podcast(self, request, queryset):
        rows_updated = queryset.update(is_podcast=False)
        self.message_user(request, '{} program(mer) er ikke lenger markert som podkast'
                          .format(rows_updated))

    unmake_podcast.short_description = 'Fjern podkast-markering'


@admin.register(Episode)
class EpisodeAdmin(admin.ModelAdmin):
    list_display = ('title', 'show', 'publish_at')
    list_filter = (ActiveShowFilter, ArchivedShowFilter)
    search_fields = ('title', 'show__name')
    form = EpisodeAdminForm


@admin.register(HighlightedPost)
class HighlightedPostAdmin(SingletonModelAdmin):
    form = HighlightedPostAdminForm
