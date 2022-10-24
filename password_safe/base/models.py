from django.db import models
from django.contrib.auth.models import User


class StoredPassword(models.Model):
    #user       = models.ForeignKey(User, on_delete=models.Cascade, null=True, blank=True)
    title       = models.CharField(max_length=30)
    password    = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)
    created     = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
