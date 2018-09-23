from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from graphene_django.views import GraphQLView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^graphql', GraphQLView.as_view(graphiql=True)),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
] + static(
    settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
