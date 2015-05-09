from django.shortcuts import render
from django.template import Context
from django.template.loader import get_template, render_to_string
from django.http import HttpResponse


def index(request):
    context = {"subtitle": "Home", "body_content": render_to_string("Home/Index.html")}
    return render(request, "Layout.html", context)