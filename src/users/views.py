from django.http import HttpResponse
from django.shortcuts import render
from django.views import View


def user_hello(request):
    return HttpResponse("<h1>Users Hello</h1>")


class UsersMain(View):
    template_name = "users/users_main.html"

    def get(self, request):
        return render(request, self.template_name)
