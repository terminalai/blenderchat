from django.db import models

# Create your models here.

class Message(models.Model):
    user = models.TextField()
    bot = models.TextField()
