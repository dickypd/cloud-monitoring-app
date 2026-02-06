import psutil
from fastapi import FastAPI

app = FastAPI()

# Endpoint utama
@app.get("/")
def home():
    return {"message": "Cloud Monitoring App Running 🚀"}

# 🔥 Endpoint metrics (INI YANG KAMU CARI)
@app.get("/metrics")
def metrics():
    return {
        "cpu_usage_percent": psutil.cpu_percent(),
        "memory_usage_percent": psutil.virtual_memory().percent
    }
