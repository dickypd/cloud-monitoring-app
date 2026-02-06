from fastapi import FastAPI
import psutil
import socket

app = FastAPI()

@app.get("/")
def home():
    return {"status": "Monitoring Service Active"}

@app.get("/metrics")
def metrics():
    return {
        "cpu_usage": psutil.cpu_percent(),
        "memory_usage": psutil.virtual_memory().percent,
        "hostname": socket.gethostname()
    }
