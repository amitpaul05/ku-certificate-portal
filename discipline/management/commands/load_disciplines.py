from django.core.management.base import BaseCommand
from discipline.models import Discipline
from utils.helpers.discipline_list import DISCIPLINES


class Command(BaseCommand):
    help = "Load the database with default disciplines."

    def handle(self, *args, **kwargs):
        for item in DISCIPLINES:
            discipline, created = Discipline.objects.get_or_create(
                discipline_code=item["discipline_code"],
                defaults={"name": item["name"]}
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f"Discipline '{item['name']}' added."))
            else:
                self.stdout.write(self.style.WARNING(f"Discipline '{item['name']}' already exists."))
