from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class News_post(models.Model):

    title = models.CharField(
        max_length=100,
        verbose_name='Заголовок новости',
        help_text='Не более 100 символов'
    )

    short_description = models.CharField(
        max_length=200,
        verbose_name='Краткое описание',
        blank=True
    )

    text = models.TextField(
        verbose_name='Полный текст новости'
    )


    pub_date = models.DateTimeField(
        verbose_name='Дата публикации',
        default=timezone.now
    )


    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Автор',
        related_name='news_posts'
    )


    is_published = models.BooleanField(
        default=True,
        verbose_name='Опубликовано'
    )


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['-pub_date']  