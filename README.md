# Automated Deployment System
Flask + Docker Compose demo showing repeatable deployment of a web service.

## Run
`cp .env.example .env && docker compose up --build -d`
Test: `curl http://localhost:5001/health`

## Deploy / update
Edit `APP_VERSION` in `.env`, then run `./scripts/deploy.sh`.
Rollback by setting the previous version and running `docker compose up -d`.

This is a local learning deployment. Add registry publishing, secrets, TLS, and a remote deployment target before production use.
