from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from rest_framework.views import APIView

from chat.models import Message
from chat.serializers import MessageSerializer, MessageDetailSerializer
from django.conf import settings


__all__ = [
    'MessageCreateAPIView',
    'MessagePaginatedListAPIView',
    'SingleMessageAPIView',
]


class MessageCreateAPIView(CreateAPIView):
    """
    View for creating message
    """
    serializer_class = MessageSerializer


class MessagePaginatedListAPIView(APIView):
    """
    View displays list of all messages with custom pagination
    """

    def get(self, *args, **kwargs):

        page_number = kwargs['page_number']

        page_size = settings.PAGINATION_PAGE_SIZE

        messages = Message.objects.all()[page_number * page_size:(page_number + 1) * page_size]

        return Response(
            data=MessageSerializer(messages, many=True).data,
            status=HTTP_200_OK,
        )


class SingleMessageAPIView(RetrieveAPIView):
    """
    View displays single message with all detail
    """
    queryset = Message.objects.all()
    serializer_class = MessageDetailSerializer

