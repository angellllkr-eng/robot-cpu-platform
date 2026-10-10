FROM python:3.12-slim

WORKDIR /app
COPY pyproject.toml ./
COPY packages ./packages
COPY apps/mindreply-gateway ./apps/mindreply-gateway

RUN pip install --no-cache-dir -e . httpx

EXPOSE 9101
CMD ["uvicorn", "apps.mindreply-gateway.main:app", "--host", "0.0.0.0", "--port", "9101"]
