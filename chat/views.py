from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView

from .models import Message
from .serializers import MessageSerializer, MessageDetailSerializer

from chat_room.pagination import CustomPagination


class MessageCreateAPIView(CreateAPIView):
    serializer_class = MessageSerializer


class MessageListAPIView(ListAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    pagination_class = CustomPagination


class SingleMessageAPIView(RetrieveAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageDetailSerializer
