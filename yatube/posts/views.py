from django.http import HttpResponse
# Импортируем загрузчик.
from django.template import loader

def index(request):
    template = loader.get_template('posts\\index.html')
    title = 'Это главная страница проекта Yatube'
    # Словарь с данными принято называть context
    context = {
        'title': title,
        'text': 'Главная страница',
    }
    #return render(request, template, context)
    return HttpResponse(template.render(context, request))


def groups_list(request):
    template = loader.get_template('posts\\group_list.html')
    title = 'Здесь будет информация о группах проекта Yatube'
    # Словарь с данными принято называть context
    context = {
        'title': title,
        'text': 'Страница групп',
    }
    # return render(request, template, context)
    return HttpResponse(template.render(context, request))


# В урл мы ждем парметр, и нужно его прередать в функцию для использования
def group_detail(request, pk):
    return HttpResponse(f'Группа {pk}')
