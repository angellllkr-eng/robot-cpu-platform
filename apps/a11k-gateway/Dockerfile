FROM python:3.12-slim

WORKDIR /app
COPY pyproject.toml ./
COPY packages ./packages
COPY apps/a11k-gateway ./apps/a11k-gateway

RUN pip install --no-cache-dir -e . httpx

EXPOSE 9001
CMD ["uvicorn", "apps.a11k-gateway.main:app", "--host", "0.0.0.0", "--port", "9001"]
