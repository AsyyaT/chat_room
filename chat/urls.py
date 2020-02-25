from django.urls import path

from .views import MessageListAPIView, SingleMessageAPIView, MessageCreateAPIView

urlpatterns = [
    path('messages/create/', MessageCreateAPIView.as_view(), name='message_create'),
    path('messages/list/', MessageListAPIView.as_view(), name='message_list'),
    path('messages/single/<int:pk>', SingleMessageAPIView.as_view(), name='message_detail'),
]

