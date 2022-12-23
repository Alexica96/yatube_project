from django.http import HttpResponse
# Импортируем загрузчик.
from django.template import loader
from .models import Post
from django.shortcuts import render


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


    #return HttpResponse(template.render(context, request))


def groups_list(request):
    posts = Post.objects.all()
    # В словаре context отправляем информацию в шаблон
    context = {
        'posts': posts,
    }
    return render(request, 'posts/group_list.html', context)


# В урл мы ждем парметр, и нужно его прередать в функцию для использования
def group_detail(request, pk):
    return HttpResponse(f'Группа {pk}')
