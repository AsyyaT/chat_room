from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView

from .models import Message
from .serializers import MessageSerializer, MessageDetailSerializer

from chat_room.pagination import CustomPagination


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
    View displays list of messages 10 per page
    """
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    pagination_class = CustomPagination


class SingleMessageAPIView(RetrieveAPIView):
    """
    View displays single message with all detail
    """
    queryset = Message.objects.all()
    serializer_class = MessageDetailSerializer
