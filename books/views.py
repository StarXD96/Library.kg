from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from . import models
from datetime import datetime
import random


def book_list_view(request):
    if request.method == 'GET':
        books = models.Books.objects.all()
        context = {
            'books': books,
        }
        return render(request, template_name='books_list/book_list.html', context=context)


def book_detail_view(request, id):
    if request.method == 'GET':
        book_id = get_object_or_404(models.Books, id=id)
        context = {
            'book_id': book_id,
        }
        return render(request, template_name='books_list/book_detail.html', context=context)


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