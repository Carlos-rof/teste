from django.db import models

class SendMsg(models.Model):
    chat_id = models.TextField()
    message = models.TextField()
    date = models.DateTimeField()
