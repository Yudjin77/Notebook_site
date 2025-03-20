from django.contrib import admin
from django.urls import path, include
from learning_logs.views import page_not_found

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("learning_logs.urls")),
    # path('users/', include('users.urls')),
]

handler404 = page_not_found