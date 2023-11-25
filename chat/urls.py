from django.urls import path
from .views import chat_room, get_messages, post_message
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('chat/<str:room_name>/', chat_room, name='chat_room'),
    path('chat/<str:room_name>/get_messages/', get_messages, name='get_messages'),
    path('chat/<str:room_name>/post_message/', post_message, name='post_message'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)