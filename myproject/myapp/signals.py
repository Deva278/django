from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
import time

@receiver(post_save, sender=User)
def user_post_save_handler(sender, instance, **kwargs):
    print(f"Signal handler triggered for user: {instance.username}")
    time.sleep(5)  # Simulates a time-consuming task
    print(f"Signal handler finished for user: {instance.username}")
