from django.test import TestCase, Client
from django.contrib.auth.models import User
from .models import Dealer, CarMake, CarModel

class DealerApiTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.dealer = Dealer.objects.create(full_name="Test Motors", city="Wichita", state="Kansas")
        make = CarMake.objects.create(name="TestMake")
        CarModel.objects.create(make=make, name="TestModel", year=2025)

    def test_get_dealers(self):
        response = self.client.get("/djangoapp/get_dealers/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()["dealers"]), 1)

    def test_filter_kansas(self):
        response = self.client.get("/djangoapp/get_dealers/Kansas/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()["dealers"]), 1)

    def test_dealer_details(self):
        response = self.client.get(f"/djangoapp/get_dealer_details/{self.dealer.id}/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["dealer"]["full_name"], "Test Motors")

    def test_sentiment_positive(self):
        response = self.client.post("/djangoapp/analyze_review/", data='{"review":"Fantastic services"}',
                                    content_type="application/json")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["sentiment"], "positive")

    def test_register(self):
        response = self.client.post("/djangoapp/register/",
            data='{"username":"tester","password":"StrongPass123","first_name":"Test","last_name":"User","email":"test@example.com"}',
            content_type="application/json")
        self.assertEqual(response.status_code, 201)
        self.assertTrue(User.objects.filter(username="tester").exists())
