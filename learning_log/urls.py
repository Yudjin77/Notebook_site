from django.contrib import admin
from django.urls import path, include
from learning_log import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("learning_logs.urls")),
    path("__debug__/", include("debug_toolbar.urls"))
    # path('users/', include('users.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


admin.site.site_header = "Панель Администрирования"
admin.site.index_title = "Известные люди мира"