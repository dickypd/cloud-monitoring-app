FROM python:3.11

WORKDIR /app

# Copy dependency file
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy semua source code
COPY . .

# Jalankan FastAPI pakai port dari Railway
CMD uvicorn app:app --host 0.0.0.0 --port $PORT
