import os

from django.http import HttpResponse
from django.shortcuts import render, reverse
import pytz
import datetime

def home_view(request):
    template_name = 'app/home.html'
    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': reverse('time'),
        'Показать содержимое рабочей директории': reverse('workdir')
    }
    context = {'pages': pages}
    return render(request, template_name, context)


def time_view(request):
    tz_belarus = pytz.timezone("Europe/Minsk")
    current_time = datetime.datetime.now(tz_belarus)
    msg = f'Текущее время: {current_time}'
    return HttpResponse(msg)


def workdir_view(request):
    template_name = 'app/workdir.html'
    workdir_list = os.listdir()
    context = {'workdir_list': workdir_list}
    return render(request, template_name, context)

