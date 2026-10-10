FROM python:3.12-slim

WORKDIR /app
COPY pyproject.toml ./
COPY packages ./packages
COPY services/commerce-service ./services/commerce-service

RUN pip install --no-cache-dir -e .

EXPOSE 8102
CMD ["uvicorn", "services.commerce-service.main:app", "--host", "0.0.0.0", "--port", "8102"]
