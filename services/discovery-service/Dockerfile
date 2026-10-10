FROM python:3.12-slim

WORKDIR /app
COPY pyproject.toml ./
COPY packages ./packages
COPY services/discovery-service ./services/discovery-service

RUN pip install --no-cache-dir -e .

EXPOSE 8101
CMD ["uvicorn", "services.discovery-service.main:app", "--host", "0.0.0.0", "--port", "8101"]
