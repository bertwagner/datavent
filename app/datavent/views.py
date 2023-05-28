from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

from django.template import loader


def index(request):
    #return HttpResponse("Hello, world. You're at the polls index.")
    return render(request, "datavent/index.html")
