from django.db import models

from applications.constants import (
    NAME_MAX_LENGTH,
    PHONE_MAX_LENGTH,
    STATUS_MAX_LENGTH,
    TITLE_MAX_LENGTH,
    TRUNCATE_TITLE_LENGTH
)


class Request(models.Model):
    class Status(models.TextChoices):
        NEW = 'new', 'Новая'
        IN_PROGRESS = 'in_progress', 'В работе'
        DONE = 'done', 'Выполнена'

    client_name = models.CharField(
        'Имя клиента',
        max_length=NAME_MAX_LENGTH,
    )
    phone = models.CharField(
        'Телефон',
        max_length=PHONE_MAX_LENGTH,
    )
    email = models.EmailField(
        'Почта',
    )
    title = models.CharField(
        'Тема обращения',
        max_length=TITLE_MAX_LENGTH,
    )
    text = models.TextField(
        'Текст обращения',
    )
    status = models.CharField(
        'Статус',
        choices=Status.choices,
        default=Status.NEW,
        max_length=STATUS_MAX_LENGTH,
    )
    created_at = models.DateTimeField(
        'Дата создания',
        auto_now_add=True,
    )

    class Meta:
        verbose_name = 'заявка'
        verbose_name_plural = 'Заявки'
        ordering = ('-created_at',)

    def __str__(self):
        return f'{self.client_name} - {self.title[:TRUNCATE_TITLE_LENGTH]}'
