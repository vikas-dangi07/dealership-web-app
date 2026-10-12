from django.contrib import admin
from .models import Dealer, Review, CarMake, CarModel

class ReviewInline(admin.TabularInline):
    model = Review
    extra = 0

@admin.register(Dealer)
class DealerAdmin(admin.ModelAdmin):
    list_display = ("full_name", "city", "state", "phone")
    search_fields = ("full_name", "city", "state")
    list_filter = ("state",)
    inlines = [ReviewInline]

class CarModelInline(admin.TabularInline):
    model = CarModel
    extra = 1

@admin.register(CarMake)
class CarMakeAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)
    inlines = [CarModelInline]

@admin.register(CarModel)
class CarModelAdmin(admin.ModelAdmin):
    list_display = ("name", "make", "year")
    list_filter = ("make", "year")

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ("dealer", "author", "sentiment", "created_at")
    list_filter = ("sentiment", "created_at")
