from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms
from django.contrib import admin
from solo.admin import SingletonModelAdmin
from sorl_cropping import ImageCroppingMixin

from .models import Category, Episode, Post, Settings, Show


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
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Post
        fields = '__all__'


class SettingsAdminForm(forms.ModelForm):
    about = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Settings
        fields = '__all__'


@admin.register(Post)
class PostAdmin(ImageCroppingMixin, admin.ModelAdmin):
    list_display = ('title', 'show', 'publish_at', 'deleted')
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
    list_display = ('name', 'archived')
    list_filter = ('archived', )
    ordering = ('archived', 'name')
    search_fields = ('name', )

    # Set form field for "lead" to Textarea instead of Textinput
    def formfield_for_dbfield(self, db_field, **kwargs):
        formfield = super(ShowAdmin, self).formfield_for_dbfield(db_field, **kwargs)
        if db_field.name == 'lead':
            formfield.widget = forms.Textarea(attrs={'cols': 40, 'rows': 3})
        return formfield


@admin.register(Episode)
class EpisodeAdmin(admin.ModelAdmin):
    list_display = ('title', 'show', 'publish_at')
    list_filter = (ActiveShowFilter, ArchivedShowFilter)
    search_fields = ('title', 'show__name')

    # Set form field for "lead" to Textarea instead of Textinput
    def formfield_for_dbfield(self, db_field, **kwargs):
        formfield = super(EpisodeAdmin, self).formfield_for_dbfield(db_field, **kwargs)
        if db_field.name == 'lead':
            formfield.widget = forms.Textarea(attrs={'cols': 60, 'rows': 5})
        return formfield
