# Deployment guide

This app can run locally and in Docker. A real public deployment requires your cloud account, configuration, and successful build; this repository intentionally does not invent a deployment URL.

## Production environment variables
Set:
- `DJANGO_SECRET_KEY`: long random secret
- `DJANGO_DEBUG=0`
- `DJANGO_ALLOWED_HOSTS`: comma-separated real hostname(s)
- Configure a persistent production database before using real customer data.

## Docker
```bash
docker compose up --build
```

## Generic cloud deployment
1. Push the repository to your own public GitHub repository.
2. Create a web service/container app from that repository.
3. Set the environment variables above and configure the service to listen on the platform's port.
4. Run `python manage.py migrate` and `python manage.py seed_demo` as a one-time release task.
5. Create an admin user securely using the platform shell or a secure one-time management command.
6. Open the provided HTTPS URL, test API routes and authentication, then save that real URL in `submission/deploymentURL`.
7. Capture the four deployed screenshots requested by the course.
8. Do not expose the demo account or use demo credentials in production.
