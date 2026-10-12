from django.conf import settings
from django.db import models

class Dealer(models.Model):
    full_name = models.CharField(max_length=160)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100, db_index=True)
    address = models.CharField(max_length=250, blank=True)
    phone = models.CharField(max_length=40, blank=True)
    website = models.URLField(blank=True)

    def __str__(self):
        return f"{self.full_name} ({self.city}, {self.state})"

class Review(models.Model):
    dealer = models.ForeignKey(Dealer, on_delete=models.CASCADE, related_name="reviews")
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="dealer_reviews")
    review = models.TextField()
    purchase = models.BooleanField(default=False)
    purchase_date = models.DateField(null=True, blank=True)
    car_make = models.CharField(max_length=100, blank=True)
    car_model = models.CharField(max_length=100, blank=True)
    sentiment = models.CharField(max_length=20, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"Review by {self.author} for {self.dealer}"

class CarMake(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class CarModel(models.Model):
    make = models.ForeignKey(CarMake, on_delete=models.CASCADE, related_name="models")
    name = models.CharField(max_length=100)
    year = models.PositiveIntegerField(default=2025)

    class Meta:
        unique_together = ("make", "name", "year")

    def __str__(self):
        return f"{self.year} {self.make.name} {self.name}"
