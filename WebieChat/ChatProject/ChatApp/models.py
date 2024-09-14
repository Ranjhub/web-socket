# chat/models.py

from django.db import models
from django.contrib.auth.models import User

class Rooms(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Messages(models.Model):
    room = models.ForeignKey(Rooms, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Add this field
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username}: {self.message}'
