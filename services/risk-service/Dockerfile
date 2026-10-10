FROM python:3.12-slim

WORKDIR /app
COPY pyproject.toml ./
COPY packages ./packages
COPY services/risk-service ./services/risk-service

RUN pip install --no-cache-dir -e .

EXPOSE 8003
CMD ["uvicorn", "services.risk-service.main:app", "--host", "0.0.0.0", "--port", "8003"]
