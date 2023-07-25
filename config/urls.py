from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("newspaper/", include("newspaper.urls", namespace="newspaper")),
    path("accounts/", include("django.contrib.auth.urls"))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
