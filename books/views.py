from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
import random



# Показывает время после запуска
def current_time_view(request):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    if request.method == 'GET':
        return HttpResponse(f'{now}')


# Случайное число от 1 до 100
def random_number_view(request):
    random_number = random.randint(1, 100)
    if request.method == 'GET':
        return HttpResponse(f'{random_number}')
    

# О себе
def about_myself_view(request):
    if request.method == 'GET':
        return HttpResponse('Меня зовут Чынтемир. Мне 17 лет и скоро исполниться 18,' \
        ' начал увлекаться программированем уже в 6-7 классе блогодаря сестре которая тоже стала программистом,' \
        ' но до сегодняшных дней не изучал. Никаких особенностей не имею' \
        ' и мои хобби довольно стандартны, по-типу играть в игры, немного почитать книг и т.д.' \
        ' Понравилась профессия программирования в основном из-за того что вижу себя как человек который' \
        ' близок к технике и хотел бы работать за ноутбуком то-есть программировать, о своем решении не жалею.')