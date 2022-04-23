from django.http import HttpResponse
from django.views import View


class Index(View):
    # template_name = "users/users_main.html"
    def get(self, request):
        return HttpResponse("<h1>index</h1>")
