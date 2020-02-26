from django.urls import path

from .views import SingleMessageAPIView, MessageCreateAPIView, MessagePaginatedListAPIView

urlpatterns = [
    path('messages/create/', MessageCreateAPIView.as_view(), name='message_create'),
    path('messages/list/<int:page_number>', MessagePaginatedListAPIView.as_view(), name='message_list'),
    path('messages/single/<int:pk>', SingleMessageAPIView.as_view(), name='message_detail'),
]

