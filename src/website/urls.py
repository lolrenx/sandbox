from django.contrib import admin
from django.urls import include, path

from .views import Index

urlpatterns = [
    path("", Index.as_view(), name="index"),
    path("admin/", admin.site.urls),
    path("users/", include("users.urls")),
]
