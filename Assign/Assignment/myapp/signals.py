from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.timezone import now
from django.core.management.base import BaseCommand
from myapp.models import MyModel

@receiver(post_save, sender=MyModel)
def my_signal_handler(sender, instance, **kwargs):
    import time
    print(f'Starting signal handler at {now()}')
    time.sleep(5)  # Simulating a long-running process
    print(f'Ending signal handler at {now()}')

class Command(BaseCommand):
    def handle(self, *args, **options):
        print(f'Starting command at {now()}')
        # Create an instance of MyModel, which triggers the signal
        MyModel.objects.create(name='test')
        print(f'Ending command at {now()}')

