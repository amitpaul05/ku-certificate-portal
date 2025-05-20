from django.core.management.base import BaseCommand
from hall.models import Hall
from utils.helpers.hall_list import HALLS


class Command(BaseCommand):
    help = "Load the database with default halls."

    def handle(self, *args, **kwargs):
        for item in HALLS:
            hall, created = Hall.objects.get_or_create(name=item["name"])
            if created:
                self.stdout.write(self.style.SUCCESS(f"Hall '{item['name']}' added."))
            else:
                self.stdout.write(self.style.WARNING(f"Hall '{item['name']}' already exists."))
