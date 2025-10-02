from django.db import models


class Books(models.Model):
    title = models.CharField(max_length=100, verbose_name='Укажите название книги')
    image = models.ImageField(upload_to='books/', verbose_name='Загрузите обложку книги')
    quantity_page = models.PositiveIntegerField(default=1, verbose_name='Укажите количество страниц')
    author = models.CharField(max_length=100, verbose_name='Укажите писателя')
    audio_book = models.URLField(verbose_name='Ссылка на аудио книгу')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Книгу'
        verbose_name_plural = 'Книги'