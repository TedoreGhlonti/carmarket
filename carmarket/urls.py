#project/urls.py

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.views.static import serve

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pages.urls')),
    path('accounts/', include('accounts.urls')),
    path('cars/', include('cars.urls')),
]

# media serving პირდაპირ - static() helper-ის გვერდის ავლით,
# რომელიც production-ში (DEBUG=False) თავისით უარს ამბობს
urlpatterns += [
    path('media/<path:path>', serve, {'document_root': settings.MEDIA_ROOT}),
]
