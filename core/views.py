from django.shortcuts import render
from django.http import HttpResponse
import datetime


def index(request):
    now = datetime.datetime.now()
    stroka = f"Now {now}"
    return HttpResponse(stroka)


def show(request):
    html = "<html>" \
           "<body>" \
           "<h1>Hello!!!</h1><br>" \
           "<p>Чтобы увидеть время сейчас перейдите по ссылке '/time'</p><br>" \
           "</body>" \
           "</html>"
    return HttpResponse(html)
