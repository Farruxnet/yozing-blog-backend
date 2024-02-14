from django.core.management.base import BaseCommand
from yozing.models import Yozing


class Command(BaseCommand):
    help = 'Bulk create objects from a CSV file'

    def handle(self, *args, **options):
        Yozing.objects.all().delete()
        self.stdout.write(self.style.SUCCESS('Deleted all Yozing objects'))
