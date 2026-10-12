# cURL examples

Start the server, migrate the database and seed data first. These examples assume `http://127.0.0.1:8000`.

## All dealers
```bash
curl -i http://127.0.0.1:8000/djangoapp/get_dealers/
```
## Dealers in Kansas
```bash
curl -i http://127.0.0.1:8000/djangoapp/get_dealers/Kansas/
```
## Dealer details
```bash
curl -i http://127.0.0.1:8000/djangoapp/get_dealer_details/1/
```
## Dealer reviews
```bash
curl -i http://127.0.0.1:8000/djangoapp/get_dealer_reviews/1/
```
## Car makes and models
```bash
curl -i http://127.0.0.1:8000/djangoapp/get_cars/
```
## Sentiment analysis
```bash
curl -i -X POST http://127.0.0.1:8000/djangoapp/analyze_review/ -H "Content-Type: application/json" -d "{\"review\":\"Fantastic services\"}"
```
## Login (save cookie for authenticated requests)
```bash
curl -i -c cookies.txt -X POST http://127.0.0.1:8000/djangoapp/login/ -H "Content-Type: application/json" -d "{\"username\":\"demo\",\"password\":\"DemoPass123!\"}"
```
## Logout
```bash
curl -i -b cookies.txt -X POST http://127.0.0.1:8000/djangoapp/logout/
```
## Register
```bash
curl -i -X POST http://127.0.0.1:8000/djangoapp/register/ -H "Content-Type: application/json" -d "{\"username\":\"sampleuser\",\"first_name\":\"Sample\",\"last_name\":\"User\",\"email\":\"sample@example.com\",\"password\":\"ChangeMe123!\"}"
```
## Add review (after login; substitute a real dealer ID)
```bash
curl -i -b cookies.txt -X POST http://127.0.0.1:8000/djangoapp/add_review/ -H "Content-Type: application/json" -d "{\"dealer_id\":1,\"review\":\"Fantastic services\",\"purchase\":true,\"car_make\":\"Toyota\",\"car_model\":\"Camry\"}"
```

Windows PowerShell note: use `curl.exe` if `curl` is aliased to `Invoke-WebRequest`. JSON quoting differs between shells.
