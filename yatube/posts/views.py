from django.shortcuts import render
from .models import Post
# Create your views here.
# Главная страница


def index(request):
    # Одна строка вместо тысячи слов на SQL:
    # в переменную posts будет сохранена выборка из 10 объектов модели Post,
    # отсортированных по полю pub_date по убыванию (от больших значений к меньшим)
    posts = Post.objects.order_by('-pub_date')[:10]
    # В словаре context отправляем информацию в шаблон
    context = {
        'posts': posts,
    }
    return render(request, 'posts/index.html', context) 


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
