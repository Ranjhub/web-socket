# chat/views.py

from django.shortcuts import render, get_object_or_404
from .models import Rooms, Messages

def room_list(request):
    rooms = Rooms.objects.all()
    return render(request, 'room_list.html', {'rooms': rooms})

def room(request, room_name):
    room, created = Rooms.objects.get_or_create(name=room_name)
    messages = Messages.objects.filter(room=room).order_by('timestamp')
    return render(request, 'chat.html', {
        'room_name': room_name,
        'messages': messages,
        'user': request.user  # Pass the current user to the template
    })
