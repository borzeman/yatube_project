from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    template = 'posts/index.html'
    head_var = "Это главная страница проекта Yatube"
    context = {
        'head_var': head_var
    }
    return render(request, template, context)

def group_post(request):
    template = 'posts/group_post.html'
    head_var = "Здесь будет информация о группах проекта Yatube"
    context = {
        'head_var': head_var
    }
    return render(request, template, context)

def group_list(request):
    template = 'posts/group_list.html'
    return render(request, template)