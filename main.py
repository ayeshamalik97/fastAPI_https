from fastapi import FastAPI

app = FastAPI(title="My HTTPS API")


@app.get("/")
def home():
    return {
        "message": "Hello! FastAPI HTTPS Server is running."
    }


@app.get("/health")
def health():
    return {
        "status": "OK"
    }