from rest_framework import serializers
import re
from chat.models import Message

__all__ = [
    'MessageSerializer',
    'MessageDetailSerializer',
]


def validate_email(value):
    if not re.match(r"^\w+([-]?\w+)*@\w+([-]?\w+)*(\.\w{2,3})+$", value):
        raise serializers.ValidationError("Your email is not valid.")
    return value


def validate_text(value):
    # if not re.match(r"^(?=[\S\s]{1,100}$)[\S\s]*", value):
    if not re.match(r"^(?=.{1,100}$).*", value):
        raise serializers.ValidationError(
            "Your text is not valid. The number of characters can't be more than one hundred."
        )
    return value


class MessageSerializer(serializers.ModelSerializer):
    """
    MessageSerializer for create message and list of messages serializer
    """
    email = serializers.EmailField(validators=[validate_email])
    text = serializers.CharField(validators=[validate_text])

    class Meta:
        model = Message
        fields = ('id', 'email', 'text')


class MessageDetailSerializer(serializers.ModelSerializer):
    """
    MessageDetailSerializer for message detail serializer
    """
    class Meta:
        model = Message
        fields = ('id', 'email', 'text', 'dt_created', 'dt_updated')

