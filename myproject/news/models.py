from django.db import models
from django.contrib.auth.models import User  # Импорт модели пользователя
from django.utils import timezone  # Для установки даты по умолчанию


class News_post(models.Model):
    # Текстовые поля
    title = models.CharField(
        max_length=100,
        verbose_name='Заголовок новости',
        help_text='Не более 100 символов'
    )

    short_description = models.CharField(
        max_length=200,
        verbose_name='Краткое описание',
        blank=True  # Необязательное поле
    )

    text = models.TextField(
        verbose_name='Полный текст новости'
    )

    # Даты и время
    pub_date = models.DateTimeField(
        verbose_name='Дата публикации',
        default=timezone.now  # Автоматическая установка текущего времени
    )

    # Связь с пользователем
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,  # При удалении пользователя удалятся его новости
        verbose_name='Автор',
        related_name='news_posts'  # Для обратных запросов
    )

    # Дополнительные поля (по желанию)
    is_published = models.BooleanField(
        default=True,
        verbose_name='Опубликовано'
    )

    # Методы
    def __str__(self):
        return self.title  # Для красивого отображения в админке

    class Meta:
        verbose_name = 'Новость'  # Название в единственном числе
        verbose_name_plural = 'Новости'  # Название во множественном числе
        ordering = ['-pub_date']  # Сортировка по дате (новые сначала)