from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator



class Tags(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

class Films(models.Model):
    image = models.ImageField(upload_to='films/', verbose_name='Загрузите картинку фильма')
    title = models.CharField(max_length=100, verbose_name='Напишите название фильма')
    description = models.TextField(verbose_name='Укажите описание к фильму')
    GENRE = (
        ('Ужасы', 'Ужасы'),
        ("Фантастика", "Фантастика"),
        ("Боевики", "Боевики")
    )
    genre = models.CharField(max_length=100, choices=GENRE, default="Фантастика")
    tags= models.ManyToManyField(Tags)
    created_at = models.DateTimeField(auto_now_add=True, null=True)


    def __str__(self):
        return self.title


    class Meta:
        verbose_name = 'фильм'
        verbose_name_plural = 'фильмы'


    def __str__(self):
        return f'{self.title}-{", ".join(i.name for i in self.tags.all())}'


class Reviews(models.Model):
    choice_film = models.ForeignKey(Films, on_delete=models.CASCADE, related_name='reviews')
    mark = models.PositiveIntegerField(verbose_name='поставьте оценку от 1 до 5', validators=[MaxValueValidator(5), MinValueValidator(1)])
    review_text = models.TextField(default='прикольный фильм')
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f'{self.choice_film} - {self.mark}'


    class Meta:
        verbose_name = 'отзыв'
        verbose_name_plural = 'отзывы'