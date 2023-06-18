from django.shortcuts import render, HttpResponse

from .models import Registration


def index(request):
    return render(request, "registration/index.html")
