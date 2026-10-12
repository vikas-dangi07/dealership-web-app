from django.urls import path
from . import views

urlpatterns = [
    path("get_dealers/", views.get_dealers, name="get_dealers"),
    path("get_dealers/<str:state>/", views.get_dealers_by_state, name="get_dealers_by_state"),
    path("get_dealer_details/<int:dealer_id>/", views.get_dealer_details, name="get_dealer_details"),
    path("get_dealer_reviews/<int:dealer_id>/", views.get_dealer_reviews, name="get_dealer_reviews"),
    path("add_review/", views.add_review, name="add_review"),
    path("get_cars/", views.get_cars, name="get_cars"),
    path("analyze_review/", views.analyze_review, name="analyze_review"),
    path("login/", views.login_user, name="login_user"),
    path("logout/", views.logout_user, name="logout_user"),
    path("register/", views.register_user, name="register_user"),
]
