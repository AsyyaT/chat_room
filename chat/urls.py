from django.urls import path

from .views import MessageListAPIView, SingleMessageAPIView, MessageCreateAPIView

urlpatterns = [
    path('messages/create/', MessageCreateAPIView.as_view()),
    path('messages/list/', MessageListAPIView.as_view()),
    path('messages/single/<int:pk>', SingleMessageAPIView.as_view()),
]

