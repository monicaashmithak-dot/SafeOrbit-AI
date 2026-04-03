FROM python:3.11-slim

WORKDIR /app

COPY safeorbit_ai.py .

CMD ["python", "safeorbit_ai.py"]