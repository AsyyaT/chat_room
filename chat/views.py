from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView

from chat.models import Message
from chat.serializers import MessageSerializer, MessageDetailSerializer

__all__ = [
    'MessageCreateAPIView',
    'MessageListAPIView',
    'SingleMessageAPIView',
]


class MessageCreateAPIView(CreateAPIView):
    """
    View for creating message
    """
    serializer_class = MessageSerializer


class MessageListAPIView(ListAPIView):
    """
    View displays list of all messages with pagination
    """
    queryset = Message.objects.all()
    serializer_class = MessageSerializer


class SingleMessageAPIView(RetrieveAPIView):
    """
    View displays single message with all detail
    """
    queryset = Message.objects.all()
    serializer_class = MessageDetailSerializer


