from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from djangoapp.models import Dealer, CarMake, CarModel, Review

class Command(BaseCommand):
    help = "Create demo dealers, car makes/models and a demo account for local testing."

    def handle(self, *args, **options):
        dealer_data = [
            ("Prairie Auto Center", "Wichita", "Kansas", "1200 Main Street", "316-555-0101"),
            ("Sunflower Motors", "Topeka", "Kansas", "45 Capital Avenue", "785-555-0102"),
            ("Lakeside Car Group", "Chicago", "Illinois", "88 Lake Road", "312-555-0103"),
            ("Desert Road Motors", "Phoenix", "Arizona", "200 Desert Drive", "602-555-0104"),
        ]
        for name, city, state, address, phone in dealer_data:
            Dealer.objects.get_or_create(full_name=name, city=city, state=state,
                defaults={"address": address, "phone": phone})
        makes = {
            "Toyota": [("Camry", 2025), ("Corolla", 2025), ("RAV4", 2024)],
            "Honda": [("Civic", 2025), ("CR-V", 2024)],
            "Ford": [("Mustang", 2025), ("Escape", 2024)],
        }
        for make_name, models in makes.items():
            make, _ = CarMake.objects.get_or_create(name=make_name)
            for model_name, year in models:
                CarModel.objects.get_or_create(make=make, name=model_name, year=year)
        demo, created = User.objects.get_or_create(username="demo")
        if created:
            demo.set_password("DemoPass123!")
            demo.first_name = "Demo"
            demo.last_name = "User"
            demo.email = "demo@example.com"
            demo.save()
        self.stdout.write(self.style.SUCCESS(
            "Demo data ready. Test account: demo / DemoPass123! (local demo only; change before deployment)."))
