from django.db import models

__all__ = [
    'Message',
]


class Message(models.Model):
    """
    Model for store users messages
    """
    email = models.EmailField(
        null=False,
        verbose_name='Email',
    )
    text = models.TextField(
        null=False,
        max_length=100,
        verbose_name='Text',
    )
    dt_created = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Date created',
    )
    dt_updated = models.DateTimeField(
        auto_now=True,
        verbose_name='Date updated',
    )
