from django.http import HttpResponse


def index(request):
    return HttpResponse('Главная страница')


def groups_list(request):
    return HttpResponse('Список групп')


# В урл мы ждем парметр, и нужно его прередать в функцию для использования
def group_detail(request, pk):
    return HttpResponse(f'Группа {pk}')
