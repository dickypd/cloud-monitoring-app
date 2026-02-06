from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"service": "Auth Service Running"}

@app.post("/login")
def login():
    return {"token": "abc123"}

@app.get("/health")
def health():
    return {"status": "ok"}
