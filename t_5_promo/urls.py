from django.conf import settings

from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static

i18n_urls = [
    path('admin/', admin.site.urls),

    path('filer/', include('filer.urls')),

    path('', include('core.urls')),
]

urlpatterns = []

urlpatterns.extend(i18n_patterns(*i18n_urls, prefix_default_language=False))
urlpatterns.extend(static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT))
