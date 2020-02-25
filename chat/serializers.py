from rest_framework import serializers
import re
from chat.models import Message


def validate_message(value):
    if not re.match(r"^\w+([-]?\w+)*@\w+([-]?\w+)*(\.\w{2,3})+$", value):
        raise serializers.ValidationError("Your email don't valid")
    return value


class MessageCreateSerializer(serializers.Serializer):
    email = serializers.EmailField(allow_null=False, allow_blank=False, validators=[validate_message])
    text = serializers.CharField(allow_blank=False, allow_null=False, max_length=100)


class MessageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Message
        fields = ('id', 'email', 'text')


class MessageDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Message
        fields = ('id', 'email', 'text', 'dt_created', 'dt_updated')

