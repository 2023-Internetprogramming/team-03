from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import ChatMessage
from django.utils.safestring import mark_safe
from django.shortcuts import get_object_or_404
import json
from ott_posts.models import Ott
from django.http import HttpResponseBadRequest

@login_required
def chat_room(request, room_name):
    room_name = room_name.strip('"')
    return render(request, 'chat/chat_room.html', {'room_name_json': mark_safe(json.dumps(room_name))})

@login_required
def get_messages(request, room_name):
    room_messages = ChatMessage.objects.filter(room=room_name).order_by('timestamp')[:50]
    messages_data = {'messages': [{'user': msg.user.username, 'message': msg.message, 'timestamp': msg.timestamp} for msg in room_messages]}
    return JsonResponse(messages_data)

@login_required
def post_message(request, room_name):
    if request.method == 'POST':
        message = request.POST.get('message', '')
        if message:
            ChatMessage.objects.create(user=request.user, message=message, room=room_name)
    return redirect('chat_room', room_name=room_name)
