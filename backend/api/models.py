from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class FeedbackForm(models.Model):
    """Основная модель хранения данных формы."""
    email = models.EmailField()
    phone = PhoneNumberField(verbose_name='номер телефона')
    message = models.TextField(
        blank=True, default='', verbose_name='сообщение'
    )

    class Meta:
        verbose_name = 'сообщение'
        verbose_name_plural = 'сообщения'
