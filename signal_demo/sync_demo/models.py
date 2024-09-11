from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
import time

class SyncModel(models.Model):
    name = models.CharField(max_length=100)

@receiver(post_save, sender=SyncModel)
def sync_signal_handler(sender, instance, created, **kwargs):
    print(f"Sync signal handler started at {time.time()}")
    time.sleep(5)  # Simulate time-consuming operation
    print(f"Sync signal handler finished at {time.time()}")