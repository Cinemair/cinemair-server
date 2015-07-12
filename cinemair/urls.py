from django.conf.urls import include, url
from django.contrib import admin

from .routers import router


urlpatterns = [
    url(r"^admin/", include(admin.site.urls)),
    url(r"^api-auth/", include("rest_framework.urls", namespace="rest_framework")),

    url(r'^api/v1/', include(router.urls)),
]
