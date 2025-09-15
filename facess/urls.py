from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, "index.html", {})


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home, name="home"),
    path("api-auth/", include("rest_framework.urls")),
    path("api/", include("usuarios.urls")),
    path("api/", include("academico.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
