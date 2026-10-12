import json
from datetime import date
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.views.decorators.http import require_GET, require_POST
from django.views.decorators.csrf import csrf_exempt
from .models import Dealer, Review, CarMake

def _json_body(request):
    try:
        return json.loads(request.body.decode("utf-8") or "{}")
    except (json.JSONDecodeError, UnicodeDecodeError):
        return {}

def _dealer_dict(d):
    return {"id": d.id, "full_name": d.full_name, "city": d.city, "state": d.state,
            "address": d.address, "phone": d.phone, "website": d.website}

def _review_dict(r):
    return {"id": r.id, "dealer_id": r.dealer_id, "author": r.author.username,
            "review": r.review, "purchase": r.purchase, "purchase_date": r.purchase_date,
            "car_make": r.car_make, "car_model": r.car_model, "sentiment": r.sentiment,
            "created_at": r.created_at.isoformat()}

@require_GET
def get_dealers(request):
    return JsonResponse({"status": 200, "dealers": [_dealer_dict(d) for d in Dealer.objects.all()]})

@require_GET
def get_dealers_by_state(request, state):
    dealers = Dealer.objects.filter(state__iexact=state.replace("-", " "))
    return JsonResponse({"status": 200, "state": state, "dealers": [_dealer_dict(d) for d in dealers]})

@require_GET
def get_dealer_details(request, dealer_id):
    try:
        dealer = Dealer.objects.get(pk=dealer_id)
    except Dealer.DoesNotExist:
        return JsonResponse({"status": 404, "message": "Dealer not found"}, status=404)
    return JsonResponse({"status": 200, "dealer": _dealer_dict(dealer),
                         "reviews": [_review_dict(r) for r in dealer.reviews.select_related("author")]})

@require_GET
def get_dealer_reviews(request, dealer_id):
    if not Dealer.objects.filter(pk=dealer_id).exists():
        return JsonResponse({"status": 404, "message": "Dealer not found"}, status=404)
    reviews = Review.objects.filter(dealer_id=dealer_id).select_related("author")
    return JsonResponse({"status": 200, "reviews": [_review_dict(r) for r in reviews]})

@csrf_exempt
@require_POST
def add_review(request):
    if not request.user.is_authenticated:
        return JsonResponse({"status": 401, "message": "Login required to post a review"}, status=401)
    data = _json_body(request)
    required = ["dealer_id", "review"]
    if any(not data.get(k) for k in required):
        return JsonResponse({"status": 400, "message": "dealer_id and review are required"}, status=400)
    try:
        dealer = Dealer.objects.get(pk=int(data["dealer_id"]))
    except (Dealer.DoesNotExist, ValueError, TypeError):
        return JsonResponse({"status": 404, "message": "Dealer not found"}, status=404)
    purchase_date = None
    if data.get("purchase_date"):
        try:
            purchase_date = date.fromisoformat(data["purchase_date"])
        except ValueError:
            return JsonResponse({"status": 400, "message": "purchase_date must use YYYY-MM-DD"}, status=400)
    text = str(data["review"]).strip()
    review = Review.objects.create(
        dealer=dealer, author=request.user, review=text,
        purchase=bool(data.get("purchase", False)), purchase_date=purchase_date,
        car_make=str(data.get("car_make", "")), car_model=str(data.get("car_model", "")),
        sentiment=_sentiment(text))
    return JsonResponse({"status": 201, "review": _review_dict(review)}, status=201)

@require_GET
def get_cars(request):
    makes = [{"id": m.id, "name": m.name,
              "models": [{"id": cm.id, "name": cm.name, "year": cm.year} for cm in m.models.all()]}
             for m in CarMake.objects.prefetch_related("models").all()]
    return JsonResponse({"status": 200, "car_makes": makes})

def _sentiment(text):
    positive = {"fantastic", "great", "excellent", "good", "amazing", "wonderful", "friendly", "helpful", "best", "love", "smooth", "perfect", "quick"}
    negative = {"bad", "terrible", "awful", "poor", "worst", "rude", "slow", "hate", "disappointing", "broken", "expensive"}
    words = {w.strip(".,!?;:").lower() for w in text.split()}
    score = len(words & positive) - len(words & negative)
    return "positive" if score > 0 else "negative" if score < 0 else "neutral"

@csrf_exempt
@require_POST
def analyze_review(request):
    data = _json_body(request)
    text = str(data.get("review", data.get("text", ""))).strip()
    if not text:
        return JsonResponse({"status": 400, "message": "review text is required"}, status=400)
    return JsonResponse({"status": 200, "review": text, "sentiment": _sentiment(text)})

@csrf_exempt
@require_POST
def login_user(request):
    data = _json_body(request)
    username, password = data.get("username", ""), data.get("password", "")
    user = authenticate(request, username=username, password=password)
    if user is None:
        return JsonResponse({"status": 401, "message": "Invalid username or password"}, status=401)
    login(request, user)
    return JsonResponse({"status": 200, "message": "Login successful", "username": user.username})

@csrf_exempt
@require_POST
def logout_user(request):
    logout(request)
    return JsonResponse({"status": 200, "message": "Logout successful"})

@csrf_exempt
@require_POST
def register_user(request):
    data = _json_body(request)
    username = str(data.get("username", "")).strip()
    password = str(data.get("password", ""))
    if not username or not password:
        return JsonResponse({"status": 400, "message": "username and password are required"}, status=400)
    if User.objects.filter(username=username).exists():
        return JsonResponse({"status": 409, "message": "Username already exists"}, status=409)
    user = User.objects.create_user(
        username=username, password=password,
        first_name=str(data.get("first_name", "")),
        last_name=str(data.get("last_name", "")),
        email=str(data.get("email", "")))
    return JsonResponse({"status": 201, "message": "Registration successful", "username": user.username}, status=201)
