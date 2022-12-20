from django.urls import path

from . import views


urlpatterns = [
    # Главная страница
    path('', views.index),
    # Список мороженого
    path('groups/', views.groups_list),
    # Подробная информация о мороженом. Ждем пременную типа int,
    # и будем использовать ее под именем pk
    path(
        'group/<slug:pk>/',
        views.group_detail
    ),
]
