from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED

from .models import Message
from .serializers import MessageSerializer, MessageDetailSerializer

from chat_room.pagination import CustomPagination


class MessageCreateAPIView(CreateAPIView):
    serializer_class = MessageSerializer

    def post(self, request, *args, **kwargs):
        serializer = MessageSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=HTTP_201_CREATED)


class MessageListAPIView(ListAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    pagination_class = CustomPagination


class SingleMessageAPIView(RetrieveAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageDetailSerializer
