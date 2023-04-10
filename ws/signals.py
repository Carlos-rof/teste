import json

from django.contrib.admin.models import LogEntry
from django.db.models.signals import post_save
from django.dispatch import receiver

from django_redis import get_redis_connection


@receiver(post_save, sender=LogEntry)
def publish_event(instance, **kwargs):
    print(instance)
    event = {
        "content_type_id": 1,
        "chat_id": instance.chat_id,
        "message": instance.message,
        # "date": instance.date
    }
    print(event)
    connection = get_redis_connection("default")
    payload = json.dumps(event)
    connection.publish("events", payload)


post_save.connect(publish_event)
