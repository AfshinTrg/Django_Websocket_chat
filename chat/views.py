from django.shortcuts import render
from django.utils.safestring import mark_safe
import json


def room(request, username):
    return render(request, 'chat/room.html', {
        'username_json': mark_safe(json.dumps(username))
    })


