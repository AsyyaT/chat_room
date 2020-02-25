from rest_framework import serializers
import re
from chat.models import Message

__all__ = [
    'MessageSerializer',
    'MessageDetailSerializer',
]


def validate_email(value):
    if not re.match(r"^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$", value):
        raise serializers.ValidationError("Your email is not valid")
    return value


class MessageSerializer(serializers.ModelSerializer):
    """
    MessageSerializer for create message and list of messages serializer
    """
    email = serializers.EmailField(validators=[validate_email])
    text = serializers.CharField(
        allow_blank=True,
        allow_null=True
    )

    class Meta:
        model = Message
        fields = ('id', 'email', 'text')

    @staticmethod
    def validate_text(obj):

        if not re.match(r"^\w+", obj):
            raise serializers.ValidationError(
                "Message must not be blank"
            )

        if not re.match(r"^(?=.{1,100}$).*", obj):
            raise serializers.ValidationError(
                "The number of characters can't be more than one hundred"
            )

        return obj


class MessageDetailSerializer(serializers.ModelSerializer):
    """
    MessageDetailSerializer for message detail serializer
    """
    class Meta:
        model = Message
        fields = ('id', 'email', 'text', 'dt_created', 'dt_updated')

