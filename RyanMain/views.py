from django.shortcuts import render
from django.template.loader import get_template, render_to_string
from django.http import HttpResponse
from RyanDotCom.settings import BASE_DIR
import os


def index(request):
    context = {"subtitle": "Home", "body_content": render_to_string("Home/Index.html")}
    return render(request, "Layout.html", context)


def resume_pdf(request):
    fsock = open(os.path.join(BASE_DIR, 'static/pdf/JohnathanHornikResume.pdf'), "rb")
    return HttpResponse(fsock, content_type="application/pdf")


def resume_docx(request):
    fsock = open(os.path.join(BASE_DIR, 'static/docx/JohnathanHornikResume.docx'), "rb")
    return HttpResponse(fsock, content_type="application/vnd.openxmlformats-officedocument.wordprocessingml.document")