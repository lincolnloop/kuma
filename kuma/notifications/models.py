from django.contrib.auth.models import User
from django.db import models


class Notification(models.Model):
    users = models.ManyToManyField(User)
    title = models.CharField(max_length=256)
    text = models.CharField(max_length=256)
    read = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def serialize(self):
        return {
            "id": self.id,
            "title": self.title,
            "text": self.text,
            "created": self.created,
            "read": False,
        }

    def __str__(self):
        return self.title
