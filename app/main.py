from fastapi import FastAPI

from app.database import Base, engine
from app.models.user import User
from app.routers.users import router as users_router
from app.routers.auth import router as auth_router


Base.metadata.create_all(bind=engine)

app = FastAPI(title="Secure FastAPI HTTPS API")


@app.get("/")
def home():
    return {
        "message": "Secure FastAPI HTTPS Server is running."
    }


@app.get("/health")
def health():
    return {
        "status": "OK"
    }


app.include_router(users_router)
app.include_router(auth_router)