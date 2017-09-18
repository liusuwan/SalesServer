from django.shortcuts import HttpResponse
from django.shortcuts import render
from sales import models

# Create your views here.
user_list = [
    {"user": "jack", "pwd": "abc"},
]


def login(request):
    if (request.method == "POST"):
        username = request.POST.get("username", None)
        password = request.POST.get("password", None)

        models.UserInfo.objects.create(user=username, pwd=password)
        global user_list
        user_list = models.UserInfo.objects.all()
        if username == "jack":
            return index(request)
        else:
            return render(request, "login.html", {"data": user_list})
    return render(request, "login.html", {"data": user_list})


def index(request):
    return render(request, "index.html")
