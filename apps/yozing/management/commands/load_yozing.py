import csv
from django.core.management.base import BaseCommand
import random
from helpers.models import Categories, Tags
from yozing.models import Yozing
from django.conf import settings


class Command(BaseCommand):
    help = 'Bulk create objects from a CSV file'
    all_categories = Categories.objects.all()
    all_tags = Tags.objects.all()

    def handle(self, *args, **options):
        csv_file_path = settings.BASE_DIR / 'data/data.csv'
        objects_to_create = []
        with open(csv_file_path, 'r', newline='', encoding='utf-8') as csvfile:
            csv_reader = csv.reader(csvfile)
            for row in csv_reader:
                name = row[1]
                text = row[2]
                random_categories = random.sample(list(self.all_categories), k=random.randint(1, len(self.all_categories)))
                random_tags = random.sample(list(self.all_tags), k=random.randint(1, len(self.all_tags)))
                obj = Yozing(name=name, text=text, image='blog-post.png', created_by_id=3)
                obj.save()
                obj.categories.set(random_categories)
                obj.tags.set(random_tags)
                objects_to_create.append(obj)
        Yozing.objects.bulk_create(objects_to_create)
        self.stdout.write(self.style.SUCCESS('Successfully created objects from CSV file'))
