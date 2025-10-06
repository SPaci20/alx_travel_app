from django.core.management.base import BaseCommand
from listings.models import Listing
import random

class Command(BaseCommand):
    help = "Seed the database with sample listings"

    def handle(self, *args, **kwargs):
        Listing.objects.all().delete()

        locations = ['Kigali', 'New York', 'Paris', 'Nairobi', 'Cape Town']
        for i in range(10):
            Listing.objects.create(
                title=f"Listing {i + 1}",
                description="A lovely place to stay.",
                price_per_night=random.randint(50, 500),
                location=random.choice(locations),
                available=random.choice([True, False]),
            )

        self.stdout.write(self.style.SUCCESS("Database seeded with sample listings!"))
