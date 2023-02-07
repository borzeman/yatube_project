from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('Основная страничка')

def group_posts(request):
    return HttpResponse('Список групп')