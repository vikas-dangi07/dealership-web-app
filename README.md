# Cars Dealership — Full-Stack Capstone Starter

A runnable Django dealership-review application with REST-style endpoints, Django Admin, review sentiment analysis, a React registration component, Docker support, and a GitHub Actions workflow.

## Important submission note
This repository is a complete **starter implementation**, not proof that all 28 graded tasks have already been completed. Real screenshots, terminal output, public GitHub URLs, CI run output, and a live deployment URL must be generated from your own running/deployed application. Do not submit placeholders as evidence.

## Requirements
- Python 3.11+
- pip
- Optional: Node.js 18+ for the React component
- Optional: Docker

## Run locally
```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py seed_demo
python manage.py runserver
```
Open http://127.0.0.1:8000/ and admin at http://127.0.0.1:8000/admin/.

## Main endpoints
- `GET /djangoapp/get_dealers/` — all dealers
- `GET /djangoapp/get_dealers/<state>/` — dealers filtered by state, e.g. `Kansas`
- `GET /djangoapp/get_dealer_details/<dealer_id>/` — dealer details
- `GET /djangoapp/get_dealer_reviews/<dealer_id>/` — reviews for a dealer
- `POST /djangoapp/add_review/` — create a review (authenticated user)
- `GET /djangoapp/get_cars/` — car makes and models
- `POST /djangoapp/analyze_review/` — sentiment for submitted review text
- `POST /djangoapp/login/` and `POST /djangoapp/logout/` — session authentication

Example:
```bash
curl http://127.0.0.1:8000/djangoapp/get_dealers/
curl http://127.0.0.1:8000/djangoapp/get_dealers/Kansas/
curl http://127.0.0.1:8000/djangoapp/get_dealer_details/1/
curl http://127.0.0.1:8000/djangoapp/get_dealer_reviews/1/
curl -X POST http://127.0.0.1:8000/djangoapp/analyze_review/ \
  -H "Content-Type: application/json" -d '{"review":"Fantastic services"}'
```

## Evidence checklist for the course
Use `submission/evidence_checklist.md` to collect the actual files/outputs requested by the assignment. The `submission/` directory contains templates and instructions, not fabricated proof.

## GitHub
Create a public repository, push this folder, then copy the real GitHub URLs for README.md, `server/frontend/static/About.html`, `server/frontend/static/Contact.html`, and `server/frontend/src/components/Register/Register.jsx`.

## Docker
```bash
docker compose up --build
```
Then visit http://127.0.0.1:8000/.

## Deployment
See `DEPLOYMENT.md`. You must deploy it using your own cloud account and put the resulting URL in `submission/deploymentURL`. No deployment URL is included because a real deployment requires your account and cloud resources.
