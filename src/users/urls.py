from django.urls import path

from .views import UsersMain

urlpatterns = [
    path("", UsersMain.as_view(), name="users_hello"),
]
