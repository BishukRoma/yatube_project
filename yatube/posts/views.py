from django.shortcuts import render

# Create your views here.
# Главная страница


def index(request):
    template = 'posts/index.html'
    text = 'Это главная страница проекта Yatube'
    context = {
        'text': text,
              }
    return render(request, template, context) 


def group_list(request):
    template = 'posts/group_list.html'
    return render(request, template) 


def group_posts(request, slug):
    template = 'posts/group_posts.html'
    text = 'Здесь будет информация о группах проекта Yatube'
    context = {
        'text': text,
        'slug': slug
              }
    return render(request, template, context) 
