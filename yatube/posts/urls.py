from django.urls import path

from . import views

# namespace должен быть объявлен при include и тут, в app_name
app_name = 'posts'

urlpatterns = [
    # Главная страница
    path('', views.index, name='main'),
    # Список мороженого
    path('groups/', views.groups_list, name='groups_list'),
    # Подробная информация о мороженом. Ждем пременную типа int,
    # и будем использовать ее под именем pk
    path(
        'group/<slug:pk>/',
        views.group_detail,
        name='group'
    ),
]
