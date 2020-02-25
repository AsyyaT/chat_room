import re

from django.core.exceptions import ValidationError
from django.db import models


def validate_message(value):
    if not re.match(r"^\w+([-]?\w+)*@\w+([-]?\w+)*(\.\w{2,3})+$", value):
        raise ValidationError("Your email don't valid")
    return value


class Message(models.Model):
    """
    Model for store users messages
    """
    email = models.EmailField(
        null=False,
        verbose_name='Email',
        # validators=[validate_message]
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
