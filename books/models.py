from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models import Avg


class Books(models.Model):
    title = models.CharField(max_length=100, verbose_name='Укажите название книги')
    image = models.ImageField(upload_to='books/', verbose_name='Загрузите обложку книги')
    quantity_page = models.PositiveIntegerField(default=1, verbose_name='Укажите количество страниц')
    author = models.CharField(max_length=100, verbose_name='Укажите писателя')
    audio_book = models.URLField(verbose_name='Ссылка на аудио книгу')
    created_at = models.DateTimeField(auto_now_add=True)

    def get_average_rating(self):
        return self.reviews.aggregate(avg=Avg('mark'))['avg'] or 0

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Книгу'
        verbose_name_plural = 'Книги'


class Reviews(models.Model):
    choice_book = models.ForeignKey(Books, on_delete=models.CASCADE, related_name='reviews')
    mark = models.PositiveIntegerField(verbose_name='Оценка от 1 до 5', validators=[MaxValueValidator(5), MinValueValidator(1)])
    review_text = models.TextField(default='Хорошая книга')
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    
    def __str__(self):
        return f'{self.choice_book} - {self.mark}'
    
    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'


class Participants(models.Model):
    name = models.CharField(max_length=100, default='Андрей')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Участника'
        verbose_name_plural = 'Участники'


class Tournaments(models.Model):
    passport = models.OneToOneField(Participants,on_delete=models.CASCADE, related_name='Participant')
    tournament_name = models.CharField(max_length=100, default='Матиматика')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.tournament_name}-{self.passport.name}'
    
    class Meta:
        verbose_name = 'Турнир'
        verbose_name_plural = 'Турниры'

