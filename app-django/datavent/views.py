from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

from django.template import loader


def index(request):
    return render(request, "datavent/index.html")


def schedule(request):
    return render(request, "datavent/schedule.html")


def code_of_conduct(request):
    return render(request, "datavent/code-of-conduct.html")
